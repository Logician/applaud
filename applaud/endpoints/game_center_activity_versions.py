from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterActivityVersionsEndpoint(Endpoint):
    path = '/v1/gameCenterActivityVersions'

    def create(self, request: GameCenterActivityVersionCreateRequest) -> GameCenterActivityVersionResponse:
        '''Create the resource.

        :param request: GameCenterActivityVersion representation
        :type request: GameCenterActivityVersionCreateRequest

        :returns: Single GameCenterActivityVersion
        :rtype: GameCenterActivityVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterActivityVersionResponse.parse_obj(json)

class GameCenterActivityVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityVersions/{id}'

    @endpoint('/v1/gameCenterActivityVersions/{id}/defaultImage')
    def default_image(self) -> DefaultImageOfGameCenterActivityVersionEndpoint:
        return DefaultImageOfGameCenterActivityVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivityVersions/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterActivityVersionEndpoint:
        return LocalizationsOfGameCenterActivityVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivityVersions/{id}/relationships/defaultImage')
    def default_image_linkage(self) -> DefaultImageLinkageOfGameCenterActivityVersionEndpoint:
        return DefaultImageLinkageOfGameCenterActivityVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivityVersions/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterActivityVersionEndpoint:
        return LocalizationsLinkagesOfGameCenterActivityVersionEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None, game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]]=None, game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]]=None) -> GameCenterActivityVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_version: the fields to include for returned resources of type gameCenterActivityVersions
        :type game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]] = None

        :param game_center_activity_localization: the fields to include for returned resources of type gameCenterActivityLocalizations
        :type game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]] = None

        :param game_center_activity_image: the fields to include for returned resources of type gameCenterActivityImages
        :type game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityVersionEndpoint
        '''
        if game_center_activity_version: self._set_fields('gameCenterActivityVersions',game_center_activity_version if type(game_center_activity_version) is list else [game_center_activity_version])
        if game_center_activity_localization: self._set_fields('gameCenterActivityLocalizations',game_center_activity_localization if type(game_center_activity_localization) is list else [game_center_activity_localization])
        if game_center_activity_image: self._set_fields('gameCenterActivityImages',game_center_activity_image if type(game_center_activity_image) is list else [game_center_activity_image])
        return self
        
    class Include(StringEnum):
        ACTIVITY = 'activity'
        LOCALIZATIONS = 'localizations'
        DEFAULT_IMAGE = 'defaultImage'
        RELEASES = 'releases'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterActivityVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None, releases: int=None) -> GameCenterActivityVersionEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityVersionEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    def get(self) -> GameCenterActivityVersionResponse:
        '''Get the resource.

        :returns: Single GameCenterActivityVersion
        :rtype: GameCenterActivityVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityVersionResponse.parse_obj(json)

    def update(self, request: GameCenterActivityVersionUpdateRequest) -> GameCenterActivityVersionResponse:
        '''Modify the resource.

        :param request: GameCenterActivityVersion representation
        :type request: GameCenterActivityVersionUpdateRequest

        :returns: Single GameCenterActivityVersion
        :rtype: GameCenterActivityVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterActivityVersionResponse.parse_obj(json)

class DefaultImageLinkageOfGameCenterActivityVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityVersions/{id}/relationships/defaultImage'

    def get(self) -> GameCenterActivityVersionDefaultImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterActivityVersionDefaultImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityVersionDefaultImageLinkageResponse.parse_obj(json)

class DefaultImageOfGameCenterActivityVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityVersions/{id}/defaultImage'

    def fields(self, *, game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]]=None) -> DefaultImageOfGameCenterActivityVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_image: the fields to include for returned resources of type gameCenterActivityImages
        :type game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.DefaultImageOfGameCenterActivityVersionEndpoint
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

class LocalizationsLinkagesOfGameCenterActivityVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityVersions/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterActivityVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterActivityVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterActivityVersionLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterActivityVersionLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityVersionLocalizationsLinkagesResponse.parse_obj(json)

class LocalizationsOfGameCenterActivityVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityVersions/{id}/localizations'

    def fields(self, *, game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]]=None, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None, game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]]=None) -> LocalizationsOfGameCenterActivityVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_localization: the fields to include for returned resources of type gameCenterActivityLocalizations
        :type game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]] = None

        :param game_center_activity_version: the fields to include for returned resources of type gameCenterActivityVersions
        :type game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]] = None

        :param game_center_activity_image: the fields to include for returned resources of type gameCenterActivityImages
        :type game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterActivityVersionEndpoint
        '''
        if game_center_activity_localization: self._set_fields('gameCenterActivityLocalizations',game_center_activity_localization if type(game_center_activity_localization) is list else [game_center_activity_localization])
        if game_center_activity_version: self._set_fields('gameCenterActivityVersions',game_center_activity_version if type(game_center_activity_version) is list else [game_center_activity_version])
        if game_center_activity_image: self._set_fields('gameCenterActivityImages',game_center_activity_image if type(game_center_activity_image) is list else [game_center_activity_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterActivityVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterActivityVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterActivityVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterActivityVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterActivityLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterActivityLocalizations
        :rtype: GameCenterActivityLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityLocalizationsResponse.parse_obj(json)

