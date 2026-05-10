from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardVersionsEndpoint(Endpoint):
    path = '/v2/gameCenterLeaderboardVersions'

    def create(self, request: GameCenterLeaderboardVersionV2CreateRequest) -> GameCenterLeaderboardVersionV2Response:
        '''Create the resource.

        :param request: GameCenterLeaderboardVersion representation
        :type request: GameCenterLeaderboardVersionV2CreateRequest

        :returns: Single GameCenterLeaderboardVersion
        :rtype: GameCenterLeaderboardVersionV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardVersionV2Response.parse_obj(json)

class GameCenterLeaderboardVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardVersions/{id}'

    @endpoint('/v2/gameCenterLeaderboardVersions/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterLeaderboardVersionEndpoint:
        return LocalizationsOfGameCenterLeaderboardVersionEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboardVersions/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterLeaderboardVersionEndpoint:
        return LocalizationsLinkagesOfGameCenterLeaderboardVersionEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None) -> GameCenterLeaderboardVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_version: the fields to include for returned resources of type gameCenterLeaderboardVersions
        :type game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]] = None

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardVersionEndpoint
        '''
        if game_center_leaderboard_version: self._set_fields('gameCenterLeaderboardVersions',game_center_leaderboard_version if type(game_center_leaderboard_version) is list else [game_center_leaderboard_version])
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        return self
        
    class Include(StringEnum):
        LEADERBOARD = 'leaderboard'
        LOCALIZATIONS = 'localizations'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None) -> GameCenterLeaderboardVersionEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardVersionEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> GameCenterLeaderboardVersionV2Response:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardVersion
        :rtype: GameCenterLeaderboardVersionV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardVersionV2Response.parse_obj(json)

    def get_all(self) -> GameCenterLeaderboardVersionV2Response:
        '''
        Get all resources.

        :returns: Single GameCenterLeaderboardVersion
        :rtype: GameCenterLeaderboardVersionV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterLeaderboardVersionV2Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterLeaderboardVersionV2Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class LocalizationsLinkagesOfGameCenterLeaderboardVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardVersions/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterLeaderboardVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterLeaderboardVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardVersionV2LocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardVersionV2LocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardVersionV2LocalizationsLinkagesResponse.parse_obj(json)

    def get_all(self) -> GameCenterLeaderboardVersionV2LocalizationsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardVersionV2LocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterLeaderboardVersionV2LocalizationsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterLeaderboardVersionV2LocalizationsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class LocalizationsOfGameCenterLeaderboardVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardVersions/{id}/localizations'

    def fields(self, *, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None, game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]]=None) -> LocalizationsOfGameCenterLeaderboardVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :param game_center_leaderboard_version: the fields to include for returned resources of type gameCenterLeaderboardVersions
        :type game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]] = None

        :param game_center_leaderboard_image: the fields to include for returned resources of type gameCenterLeaderboardImages
        :type game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardVersionEndpoint
        '''
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        if game_center_leaderboard_version: self._set_fields('gameCenterLeaderboardVersions',game_center_leaderboard_version if type(game_center_leaderboard_version) is list else [game_center_leaderboard_version])
        if game_center_leaderboard_image: self._set_fields('gameCenterLeaderboardImages',game_center_leaderboard_image if type(game_center_leaderboard_image) is list else [game_center_leaderboard_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterLeaderboardVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterLeaderboardVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardLocalizationsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardLocalizations
        :rtype: GameCenterLeaderboardLocalizationsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardLocalizationsV2Response.parse_obj(json)

    def get_all(self) -> GameCenterLeaderboardLocalizationsV2Response:
        '''
        Get all resources.

        :returns: List of GameCenterLeaderboardLocalizations
        :rtype: GameCenterLeaderboardLocalizationsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterLeaderboardLocalizationsV2Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterLeaderboardLocalizationsV2Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

