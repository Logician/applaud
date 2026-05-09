from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardSetLocalizationsEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardSetLocalizations'

    @deprecated
    def create(self, request: GameCenterLeaderboardSetLocalizationCreateRequest) -> GameCenterLeaderboardSetLocalizationResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardSetLocalization representation
        :type request: GameCenterLeaderboardSetLocalizationCreateRequest

        :returns: Single GameCenterLeaderboardSetLocalization
        :rtype: GameCenterLeaderboardSetLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetLocalizationResponse.parse_obj(json)

class GameCenterLeaderboardSetLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetLocalizations/{id}'

    @endpoint('/v1/gameCenterLeaderboardSetLocalizations/{id}/gameCenterLeaderboardSetImage')
    def game_center_leaderboard_set_image(self) -> GameCenterLeaderboardSetImageOfGameCenterLeaderboardSetLocalizationEndpoint:
        return GameCenterLeaderboardSetImageOfGameCenterLeaderboardSetLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSetLocalizations/{id}/relationships/gameCenterLeaderboardSetImage')
    def game_center_leaderboard_set_image_linkage(self) -> GameCenterLeaderboardSetImageLinkageOfGameCenterLeaderboardSetLocalizationEndpoint:
        return GameCenterLeaderboardSetImageLinkageOfGameCenterLeaderboardSetLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None) -> GameCenterLeaderboardSetLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetLocalizationEndpoint
        '''
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD_SET = 'gameCenterLeaderboardSet'
        GAME_CENTER_LEADERBOARD_SET_IMAGE = 'gameCenterLeaderboardSetImage'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterLeaderboardSetLocalizationResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSetLocalization
        :rtype: GameCenterLeaderboardSetLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetLocalizationResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterLeaderboardSetLocalizationUpdateRequest) -> GameCenterLeaderboardSetLocalizationResponse:
        '''Modify the resource.

        :param request: GameCenterLeaderboardSetLocalization representation
        :type request: GameCenterLeaderboardSetLocalizationUpdateRequest

        :returns: Single GameCenterLeaderboardSetLocalization
        :rtype: GameCenterLeaderboardSetLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardSetLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardSetLocalizationsEndpoint(Endpoint):
    path = '/v2/gameCenterLeaderboardSetLocalizations'

    def create(self, request: GameCenterLeaderboardSetLocalizationV2CreateRequest) -> GameCenterLeaderboardSetLocalizationV2Response:
        '''Create the resource.

        :param request: GameCenterLeaderboardSetLocalization representation
        :type request: GameCenterLeaderboardSetLocalizationV2CreateRequest

        :returns: Single GameCenterLeaderboardSetLocalization
        :rtype: GameCenterLeaderboardSetLocalizationV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetLocalizationV2Response.parse_obj(json)

class GameCenterLeaderboardSetLocalizationEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSetLocalizations/{id}'

    @endpoint('/v2/gameCenterLeaderboardSetLocalizations/{id}/image')
    def image(self) -> ImageOfGameCenterLeaderboardSetLocalizationEndpoint:
        return ImageOfGameCenterLeaderboardSetLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboardSetLocalizations/{id}/relationships/image')
    def image_linkage(self) -> ImageLinkageOfGameCenterLeaderboardSetLocalizationEndpoint:
        return ImageLinkageOfGameCenterLeaderboardSetLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None) -> GameCenterLeaderboardSetLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetLocalizationEndpoint
        '''
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterLeaderboardSetLocalizationV2Response:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSetLocalization
        :rtype: GameCenterLeaderboardSetLocalizationV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetLocalizationV2Response.parse_obj(json)

    def update(self, request: GameCenterLeaderboardSetLocalizationV2UpdateRequest) -> GameCenterLeaderboardSetLocalizationV2Response:
        '''Modify the resource.

        :param request: GameCenterLeaderboardSetLocalization representation
        :type request: GameCenterLeaderboardSetLocalizationV2UpdateRequest

        :returns: Single GameCenterLeaderboardSetLocalization
        :rtype: GameCenterLeaderboardSetLocalizationV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardSetLocalizationV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardSetImageLinkageOfGameCenterLeaderboardSetLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetLocalizations/{id}/relationships/gameCenterLeaderboardSetImage'

    @deprecated
    def get(self) -> GameCenterLeaderboardSetLocalizationGameCenterLeaderboardSetImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterLeaderboardSetLocalizationGameCenterLeaderboardSetImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetLocalizationGameCenterLeaderboardSetImageLinkageResponse.parse_obj(json)

class GameCenterLeaderboardSetImageOfGameCenterLeaderboardSetLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetLocalizations/{id}/gameCenterLeaderboardSetImage'

    def fields(self, *, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None) -> GameCenterLeaderboardSetImageOfGameCenterLeaderboardSetLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetImageOfGameCenterLeaderboardSetLocalizationEndpoint
        '''
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD_SET_LOCALIZATION = 'gameCenterLeaderboardSetLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetImageOfGameCenterLeaderboardSetLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetImageOfGameCenterLeaderboardSetLocalizationEndpoint
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

class ImageLinkageOfGameCenterLeaderboardSetLocalizationEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSetLocalizations/{id}/relationships/image'

    def get(self) -> GameCenterLeaderboardSetLocalizationV2ImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterLeaderboardSetLocalizationV2ImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetLocalizationV2ImageLinkageResponse.parse_obj(json)

class ImageOfGameCenterLeaderboardSetLocalizationEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSetLocalizations/{id}/image'

    def fields(self, *, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None) -> ImageOfGameCenterLeaderboardSetLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.ImageOfGameCenterLeaderboardSetLocalizationEndpoint
        '''
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        return self
        
    class Include(StringEnum):
        LOCALIZATION = 'localization'

    def include(self, relationship: Union[Include, list[Include]]) -> ImageOfGameCenterLeaderboardSetLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ImageOfGameCenterLeaderboardSetLocalizationEndpoint
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

