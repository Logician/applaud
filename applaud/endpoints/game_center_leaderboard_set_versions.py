from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardSetVersionsEndpoint(Endpoint):
    path = '/v2/gameCenterLeaderboardSetVersions'

    def create(self, request: GameCenterLeaderboardSetVersionV2CreateRequest) -> GameCenterLeaderboardSetVersionV2Response:
        '''Create the resource.

        :param request: GameCenterLeaderboardSetVersion representation
        :type request: GameCenterLeaderboardSetVersionV2CreateRequest

        :returns: Single GameCenterLeaderboardSetVersion
        :rtype: GameCenterLeaderboardSetVersionV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetVersionV2Response.parse_obj(json)

class GameCenterLeaderboardSetVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSetVersions/{id}'

    @endpoint('/v2/gameCenterLeaderboardSetVersions/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterLeaderboardSetVersionEndpoint:
        return LocalizationsOfGameCenterLeaderboardSetVersionEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboardSetVersions/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterLeaderboardSetVersionEndpoint:
        return LocalizationsLinkagesOfGameCenterLeaderboardSetVersionEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None) -> GameCenterLeaderboardSetVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_version: the fields to include for returned resources of type gameCenterLeaderboardSetVersions
        :type game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]] = None

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetVersionEndpoint
        '''
        if game_center_leaderboard_set_version: self._set_fields('gameCenterLeaderboardSetVersions',game_center_leaderboard_set_version if type(game_center_leaderboard_set_version) is list else [game_center_leaderboard_set_version])
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        return self
        
    class Include(StringEnum):
        LEADERBOARD_SET = 'leaderboardSet'
        LOCALIZATIONS = 'localizations'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None) -> GameCenterLeaderboardSetVersionEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetVersionEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> GameCenterLeaderboardSetVersionV2Response:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSetVersion
        :rtype: GameCenterLeaderboardSetVersionV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetVersionV2Response.parse_obj(json)

class LocalizationsLinkagesOfGameCenterLeaderboardSetVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSetVersions/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterLeaderboardSetVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterLeaderboardSetVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardSetVersionV2LocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardSetVersionV2LocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetVersionV2LocalizationsLinkagesResponse.parse_obj(json)

class LocalizationsOfGameCenterLeaderboardSetVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSetVersions/{id}/localizations'

    def fields(self, *, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]]=None, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None) -> LocalizationsOfGameCenterLeaderboardSetVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :param game_center_leaderboard_set_version: the fields to include for returned resources of type gameCenterLeaderboardSetVersions
        :type game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]] = None

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardSetVersionEndpoint
        '''
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        if game_center_leaderboard_set_version: self._set_fields('gameCenterLeaderboardSetVersions',game_center_leaderboard_set_version if type(game_center_leaderboard_set_version) is list else [game_center_leaderboard_set_version])
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterLeaderboardSetVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardSetVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterLeaderboardSetVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardSetVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardSetLocalizationsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardSetLocalizations
        :rtype: GameCenterLeaderboardSetLocalizationsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetLocalizationsV2Response.parse_obj(json)

