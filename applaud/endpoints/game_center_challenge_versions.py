from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterChallengeVersionsEndpoint(Endpoint):
    path = '/v1/gameCenterChallengeVersions'

    def create(self, request: GameCenterChallengeVersionCreateRequest) -> GameCenterChallengeVersionResponse:
        '''Create the resource.

        :param request: GameCenterChallengeVersion representation
        :type request: GameCenterChallengeVersionCreateRequest

        :returns: Single GameCenterChallengeVersion
        :rtype: GameCenterChallengeVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterChallengeVersionResponse.parse_obj(json)

class GameCenterChallengeVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeVersions/{id}'

    @endpoint('/v1/gameCenterChallengeVersions/{id}/defaultImage')
    def default_image(self) -> DefaultImageOfGameCenterChallengeVersionEndpoint:
        return DefaultImageOfGameCenterChallengeVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterChallengeVersions/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterChallengeVersionEndpoint:
        return LocalizationsOfGameCenterChallengeVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterChallengeVersions/{id}/relationships/defaultImage')
    def default_image_linkage(self) -> DefaultImageLinkageOfGameCenterChallengeVersionEndpoint:
        return DefaultImageLinkageOfGameCenterChallengeVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterChallengeVersions/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterChallengeVersionEndpoint:
        return LocalizationsLinkagesOfGameCenterChallengeVersionEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None, game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]]=None, game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]]=None) -> GameCenterChallengeVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_version: the fields to include for returned resources of type gameCenterChallengeVersions
        :type game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]] = None

        :param game_center_challenge_localization: the fields to include for returned resources of type gameCenterChallengeLocalizations
        :type game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]] = None

        :param game_center_challenge_image: the fields to include for returned resources of type gameCenterChallengeImages
        :type game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeVersionEndpoint
        '''
        if game_center_challenge_version: self._set_fields('gameCenterChallengeVersions',game_center_challenge_version if type(game_center_challenge_version) is list else [game_center_challenge_version])
        if game_center_challenge_localization: self._set_fields('gameCenterChallengeLocalizations',game_center_challenge_localization if type(game_center_challenge_localization) is list else [game_center_challenge_localization])
        if game_center_challenge_image: self._set_fields('gameCenterChallengeImages',game_center_challenge_image if type(game_center_challenge_image) is list else [game_center_challenge_image])
        return self
        
    class Include(StringEnum):
        CHALLENGE = 'challenge'
        LOCALIZATIONS = 'localizations'
        RELEASES = 'releases'
        DEFAULT_IMAGE = 'defaultImage'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterChallengeVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None, releases: int=None) -> GameCenterChallengeVersionEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeVersionEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    def get(self) -> GameCenterChallengeVersionResponse:
        '''Get the resource.

        :returns: Single GameCenterChallengeVersion
        :rtype: GameCenterChallengeVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeVersionResponse.parse_obj(json)

class DefaultImageLinkageOfGameCenterChallengeVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeVersions/{id}/relationships/defaultImage'

    def get(self) -> GameCenterChallengeVersionDefaultImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterChallengeVersionDefaultImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeVersionDefaultImageLinkageResponse.parse_obj(json)

class DefaultImageOfGameCenterChallengeVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeVersions/{id}/defaultImage'

    def fields(self, *, game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]]=None) -> DefaultImageOfGameCenterChallengeVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_image: the fields to include for returned resources of type gameCenterChallengeImages
        :type game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.DefaultImageOfGameCenterChallengeVersionEndpoint
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

class LocalizationsLinkagesOfGameCenterChallengeVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeVersions/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterChallengeVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterChallengeVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterChallengeVersionLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterChallengeVersionLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeVersionLocalizationsLinkagesResponse.parse_obj(json)

class LocalizationsOfGameCenterChallengeVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeVersions/{id}/localizations'

    def fields(self, *, game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]]=None, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None, game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]]=None) -> LocalizationsOfGameCenterChallengeVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_localization: the fields to include for returned resources of type gameCenterChallengeLocalizations
        :type game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]] = None

        :param game_center_challenge_version: the fields to include for returned resources of type gameCenterChallengeVersions
        :type game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]] = None

        :param game_center_challenge_image: the fields to include for returned resources of type gameCenterChallengeImages
        :type game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterChallengeVersionEndpoint
        '''
        if game_center_challenge_localization: self._set_fields('gameCenterChallengeLocalizations',game_center_challenge_localization if type(game_center_challenge_localization) is list else [game_center_challenge_localization])
        if game_center_challenge_version: self._set_fields('gameCenterChallengeVersions',game_center_challenge_version if type(game_center_challenge_version) is list else [game_center_challenge_version])
        if game_center_challenge_image: self._set_fields('gameCenterChallengeImages',game_center_challenge_image if type(game_center_challenge_image) is list else [game_center_challenge_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterChallengeVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterChallengeVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterChallengeVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterChallengeVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterChallengeLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterChallengeLocalizations
        :rtype: GameCenterChallengeLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeLocalizationsResponse.parse_obj(json)

