from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterAchievementVersionsEndpoint(Endpoint):
    path = '/v2/gameCenterAchievementVersions'

    def create(self, request: GameCenterAchievementVersionV2CreateRequest) -> GameCenterAchievementVersionV2Response:
        '''Create the resource.

        :param request: GameCenterAchievementVersion representation
        :type request: GameCenterAchievementVersionV2CreateRequest

        :returns: Single GameCenterAchievementVersion
        :rtype: GameCenterAchievementVersionV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementVersionV2Response.parse_obj(json)

class GameCenterAchievementVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievementVersions/{id}'

    @endpoint('/v2/gameCenterAchievementVersions/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterAchievementVersionEndpoint:
        return LocalizationsOfGameCenterAchievementVersionEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterAchievementVersions/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterAchievementVersionEndpoint:
        return LocalizationsLinkagesOfGameCenterAchievementVersionEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None) -> GameCenterAchievementVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_version: the fields to include for returned resources of type gameCenterAchievementVersions
        :type game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]] = None

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementVersionEndpoint
        '''
        if game_center_achievement_version: self._set_fields('gameCenterAchievementVersions',game_center_achievement_version if type(game_center_achievement_version) is list else [game_center_achievement_version])
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        return self
        
    class Include(StringEnum):
        ACHIEVEMENT = 'achievement'
        LOCALIZATIONS = 'localizations'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None) -> GameCenterAchievementVersionEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementVersionEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> GameCenterAchievementVersionV2Response:
        '''Get the resource.

        :returns: Single GameCenterAchievementVersion
        :rtype: GameCenterAchievementVersionV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementVersionV2Response.parse_obj(json)

class LocalizationsLinkagesOfGameCenterAchievementVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievementVersions/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterAchievementVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterAchievementVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterAchievementVersionV2LocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterAchievementVersionV2LocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementVersionV2LocalizationsLinkagesResponse.parse_obj(json)

class LocalizationsOfGameCenterAchievementVersionEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievementVersions/{id}/localizations'

    def fields(self, *, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]]=None, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None) -> LocalizationsOfGameCenterAchievementVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :param game_center_achievement_version: the fields to include for returned resources of type gameCenterAchievementVersions
        :type game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]] = None

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterAchievementVersionEndpoint
        '''
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        if game_center_achievement_version: self._set_fields('gameCenterAchievementVersions',game_center_achievement_version if type(game_center_achievement_version) is list else [game_center_achievement_version])
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterAchievementVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterAchievementVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterAchievementVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterAchievementVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterAchievementLocalizationsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterAchievementLocalizations
        :rtype: GameCenterAchievementLocalizationsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationsV2Response.parse_obj(json)

