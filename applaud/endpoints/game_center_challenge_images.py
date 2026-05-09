from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterChallengeImagesEndpoint(Endpoint):
    path = '/v1/gameCenterChallengeImages'

    def create(self, request: GameCenterChallengeImageCreateRequest) -> GameCenterChallengeImageResponse:
        '''Create the resource.

        :param request: GameCenterChallengeImage representation
        :type request: GameCenterChallengeImageCreateRequest

        :returns: Single GameCenterChallengeImage
        :rtype: GameCenterChallengeImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterChallengeImageResponse.parse_obj(json)

class GameCenterChallengeImageEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeImages/{id}'

    def fields(self, *, game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]]=None) -> GameCenterChallengeImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_image: the fields to include for returned resources of type gameCenterChallengeImages
        :type game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeImageEndpoint
        '''
        if game_center_challenge_image: self._set_fields('gameCenterChallengeImages',game_center_challenge_image if type(game_center_challenge_image) is list else [game_center_challenge_image])
        return self
        
    def get(self) -> GameCenterChallengeImageResponse:
        '''Get the resource.

        :returns: Single GameCenterChallengeImage
        :rtype: GameCenterChallengeImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeImageResponse.parse_obj(json)

    def update(self, request: GameCenterChallengeImageUpdateRequest) -> GameCenterChallengeImageResponse:
        '''Modify the resource.

        :param request: GameCenterChallengeImage representation
        :type request: GameCenterChallengeImageUpdateRequest

        :returns: Single GameCenterChallengeImage
        :rtype: GameCenterChallengeImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterChallengeImageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

