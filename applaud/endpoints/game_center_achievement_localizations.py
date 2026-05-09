from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterAchievementLocalizationsEndpoint(Endpoint):
    path = '/v2/gameCenterAchievementLocalizations'

    def create(self, request: GameCenterAchievementLocalizationV2CreateRequest) -> GameCenterAchievementLocalizationV2Response:
        '''Create the resource.

        :param request: GameCenterAchievementLocalization representation
        :type request: GameCenterAchievementLocalizationV2CreateRequest

        :returns: Single GameCenterAchievementLocalization
        :rtype: GameCenterAchievementLocalizationV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementLocalizationV2Response.parse_obj(json)

class GameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievementLocalizations/{id}'

    @endpoint('/v2/gameCenterAchievementLocalizations/{id}/image')
    def image(self) -> ImageOfGameCenterAchievementLocalizationEndpoint:
        return ImageOfGameCenterAchievementLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterAchievementLocalizations/{id}/relationships/image')
    def image_linkage(self) -> ImageLinkageOfGameCenterAchievementLocalizationEndpoint:
        return ImageLinkageOfGameCenterAchievementLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None) -> GameCenterAchievementLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementLocalizationEndpoint
        '''
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'
        IMAGE = 'image'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterAchievementLocalizationV2Response:
        '''Get the resource.

        :returns: Single GameCenterAchievementLocalization
        :rtype: GameCenterAchievementLocalizationV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationV2Response.parse_obj(json)

    def update(self, request: GameCenterAchievementLocalizationV2UpdateRequest) -> GameCenterAchievementLocalizationV2Response:
        '''Modify the resource.

        :param request: GameCenterAchievementLocalization representation
        :type request: GameCenterAchievementLocalizationV2UpdateRequest

        :returns: Single GameCenterAchievementLocalization
        :rtype: GameCenterAchievementLocalizationV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterAchievementLocalizationV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterAchievementLocalizationsEndpoint(Endpoint):
    path = '/v1/gameCenterAchievementLocalizations'

    @deprecated
    def create(self, request: GameCenterAchievementLocalizationCreateRequest) -> GameCenterAchievementLocalizationResponse:
        '''Create the resource.

        :param request: GameCenterAchievementLocalization representation
        :type request: GameCenterAchievementLocalizationCreateRequest

        :returns: Single GameCenterAchievementLocalization
        :rtype: GameCenterAchievementLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementLocalizationResponse.parse_obj(json)

class GameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievementLocalizations/{id}'

    @endpoint('/v1/gameCenterAchievementLocalizations/{id}/gameCenterAchievement')
    def game_center_achievement(self) -> GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint:
        return GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievementLocalizations/{id}/gameCenterAchievementImage')
    def game_center_achievement_image(self) -> GameCenterAchievementImageOfGameCenterAchievementLocalizationEndpoint:
        return GameCenterAchievementImageOfGameCenterAchievementLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievement')
    def game_center_achievement_linkage(self) -> GameCenterAchievementLinkageOfGameCenterAchievementLocalizationEndpoint:
        return GameCenterAchievementLinkageOfGameCenterAchievementLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievementImage')
    def game_center_achievement_image_linkage(self) -> GameCenterAchievementImageLinkageOfGameCenterAchievementLocalizationEndpoint:
        return GameCenterAchievementImageLinkageOfGameCenterAchievementLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None) -> GameCenterAchievementLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementLocalizationEndpoint
        '''
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_ACHIEVEMENT = 'gameCenterAchievement'
        GAME_CENTER_ACHIEVEMENT_IMAGE = 'gameCenterAchievementImage'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterAchievementLocalizationResponse:
        '''Get the resource.

        :returns: Single GameCenterAchievementLocalization
        :rtype: GameCenterAchievementLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterAchievementLocalizationUpdateRequest) -> GameCenterAchievementLocalizationResponse:
        '''Modify the resource.

        :param request: GameCenterAchievementLocalization representation
        :type request: GameCenterAchievementLocalizationUpdateRequest

        :returns: Single GameCenterAchievementLocalization
        :rtype: GameCenterAchievementLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterAchievementLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class ImageLinkageOfGameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievementLocalizations/{id}/relationships/image'

    def get(self) -> GameCenterAchievementLocalizationV2ImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterAchievementLocalizationV2ImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationV2ImageLinkageResponse.parse_obj(json)

class ImageOfGameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievementLocalizations/{id}/image'

    def fields(self, *, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None) -> ImageOfGameCenterAchievementLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.ImageOfGameCenterAchievementLocalizationEndpoint
        '''
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        return self
        
    class Include(StringEnum):
        LOCALIZATION = 'localization'

    def include(self, relationship: Union[Include, list[Include]]) -> ImageOfGameCenterAchievementLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ImageOfGameCenterAchievementLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterAchievementImageV2Response:
        '''Get the resource.

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementImageV2Response.parse_obj(json)

class GameCenterAchievementLinkageOfGameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievement'

    @deprecated
    def get(self) -> GameCenterAchievementLocalizationGameCenterAchievementLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterAchievementLocalizationGameCenterAchievementLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationGameCenterAchievementLinkageResponse.parse_obj(json)

class GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievementLocalizations/{id}/gameCenterAchievement'

    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None) -> GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :param game_center_achievement_release: the fields to include for returned resources of type gameCenterAchievementReleases
        :type game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint
        '''
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        if game_center_achievement_release: self._set_fields('gameCenterAchievementReleases',game_center_achievement_release if type(game_center_achievement_release) is list else [game_center_achievement_release])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GROUP_ACHIEVEMENT = 'groupAchievement'
        LOCALIZATIONS = 'localizations'
        RELEASES = 'releases'
        ACTIVITY = 'activity'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None, releases: int=None) -> GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementOfGameCenterAchievementLocalizationEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    @deprecated
    def get(self) -> GameCenterAchievementResponse:
        '''Get the resource.

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementResponse.parse_obj(json)

class GameCenterAchievementImageLinkageOfGameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievementImage'

    @deprecated
    def get(self) -> GameCenterAchievementLocalizationGameCenterAchievementImageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterAchievementLocalizationGameCenterAchievementImageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationGameCenterAchievementImageLinkageResponse.parse_obj(json)

class GameCenterAchievementImageOfGameCenterAchievementLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievementLocalizations/{id}/gameCenterAchievementImage'

    def fields(self, *, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None) -> GameCenterAchievementImageOfGameCenterAchievementLocalizationEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementImageOfGameCenterAchievementLocalizationEndpoint
        '''
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_ACHIEVEMENT_LOCALIZATION = 'gameCenterAchievementLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementImageOfGameCenterAchievementLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementImageOfGameCenterAchievementLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterAchievementImageResponse:
        '''Get the resource.

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementImageResponse.parse_obj(json)

