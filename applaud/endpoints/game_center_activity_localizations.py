from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterActivityLocalizationsEndpoint(Endpoint):
    path = '/v1/gameCenterActivityLocalizations'

    def create(self, request: GameCenterActivityLocalizationCreateRequest) -> GameCenterActivityLocalizationResponse:
        '''Create the resource.

        :param request: GameCenterActivityLocalization representation
        :type request: GameCenterActivityLocalizationCreateRequest

        :returns: Single GameCenterActivityLocalization
        :rtype: GameCenterActivityLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterActivityLocalizationResponse.parse_obj(json)

class GameCenterActivityLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityLocalizations/{id}'

    @endpoint('/v1/gameCenterActivityLocalizations/{id}/image')
    def image(self) -> ImageOfGameCenterActivityLocalizationEndpoint:
        return ImageOfGameCenterActivityLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivityLocalizations/{id}/relationships/image')
    def image_linkage(self) -> ImageLinkageOfGameCenterActivityLocalizationEndpoint:
        return ImageLinkageOfGameCenterActivityLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]]=None, game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]]=None) -> GameCenterActivityLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_localization: the fields to include for returned resources of type gameCenterActivityLocalizations
        :type game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]] = None

        :param game_center_activity_image: the fields to include for returned resources of type gameCenterActivityImages
        :type game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityLocalizationEndpoint
        '''
        if game_center_activity_localization: self._set_fields('gameCenterActivityLocalizations',game_center_activity_localization if type(game_center_activity_localization) is list else [game_center_activity_localization])
        if game_center_activity_image: self._set_fields('gameCenterActivityImages',game_center_activity_image if type(game_center_activity_image) is list else [game_center_activity_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterActivityLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterActivityLocalizationResponse:
        '''Get the resource.

        :returns: Single GameCenterActivityLocalization
        :rtype: GameCenterActivityLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityLocalizationResponse.parse_obj(json)

    def update(self, request: GameCenterActivityLocalizationUpdateRequest) -> GameCenterActivityLocalizationResponse:
        '''Modify the resource.

        :param request: GameCenterActivityLocalization representation
        :type request: GameCenterActivityLocalizationUpdateRequest

        :returns: Single GameCenterActivityLocalization
        :rtype: GameCenterActivityLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterActivityLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class ImageLinkageOfGameCenterActivityLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityLocalizations/{id}/relationships/image'

    def get(self) -> GameCenterActivityLocalizationImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterActivityLocalizationImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityLocalizationImageLinkageResponse.parse_obj(json)

class ImageOfGameCenterActivityLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityLocalizations/{id}/image'

    def fields(self, *, game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]]=None) -> ImageOfGameCenterActivityLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_image: the fields to include for returned resources of type gameCenterActivityImages
        :type game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.ImageOfGameCenterActivityLocalizationEndpoint
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

