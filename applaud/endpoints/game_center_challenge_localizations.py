from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterChallengeLocalizationsEndpoint(Endpoint):
    path = '/v1/gameCenterChallengeLocalizations'

    def create(self, request: GameCenterChallengeLocalizationCreateRequest) -> GameCenterChallengeLocalizationResponse:
        '''Create the resource.

        :param request: GameCenterChallengeLocalization representation
        :type request: GameCenterChallengeLocalizationCreateRequest

        :returns: Single GameCenterChallengeLocalization
        :rtype: GameCenterChallengeLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterChallengeLocalizationResponse.parse_obj(json)

class GameCenterChallengeLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeLocalizations/{id}'

    @endpoint('/v1/gameCenterChallengeLocalizations/{id}/image')
    def image(self) -> ImageOfGameCenterChallengeLocalizationEndpoint:
        return ImageOfGameCenterChallengeLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterChallengeLocalizations/{id}/relationships/image')
    def image_linkage(self) -> ImageLinkageOfGameCenterChallengeLocalizationEndpoint:
        return ImageLinkageOfGameCenterChallengeLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]]=None, game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]]=None) -> GameCenterChallengeLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_localization: the fields to include for returned resources of type gameCenterChallengeLocalizations
        :type game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]] = None

        :param game_center_challenge_image: the fields to include for returned resources of type gameCenterChallengeImages
        :type game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeLocalizationEndpoint
        '''
        if game_center_challenge_localization: self._set_fields('gameCenterChallengeLocalizations',game_center_challenge_localization if type(game_center_challenge_localization) is list else [game_center_challenge_localization])
        if game_center_challenge_image: self._set_fields('gameCenterChallengeImages',game_center_challenge_image if type(game_center_challenge_image) is list else [game_center_challenge_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterChallengeLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterChallengeLocalizationResponse:
        '''Get the resource.

        :returns: Single GameCenterChallengeLocalization
        :rtype: GameCenterChallengeLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeLocalizationResponse.parse_obj(json)

    def update(self, request: GameCenterChallengeLocalizationUpdateRequest) -> GameCenterChallengeLocalizationResponse:
        '''Modify the resource.

        :param request: GameCenterChallengeLocalization representation
        :type request: GameCenterChallengeLocalizationUpdateRequest

        :returns: Single GameCenterChallengeLocalization
        :rtype: GameCenterChallengeLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterChallengeLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class ImageLinkageOfGameCenterChallengeLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeLocalizations/{id}/relationships/image'

    def get(self) -> GameCenterChallengeLocalizationImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterChallengeLocalizationImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeLocalizationImageLinkageResponse.parse_obj(json)

class ImageOfGameCenterChallengeLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeLocalizations/{id}/image'

    def fields(self, *, game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]]=None) -> ImageOfGameCenterChallengeLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_image: the fields to include for returned resources of type gameCenterChallengeImages
        :type game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.ImageOfGameCenterChallengeLocalizationEndpoint
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

