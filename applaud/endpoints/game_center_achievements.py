from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterAchievementsEndpoint(Endpoint):
    path = '/v2/gameCenterAchievements'

    def create(self, request: GameCenterAchievementV2CreateRequest) -> GameCenterAchievementV2Response:
        '''Create the resource.

        :param request: GameCenterAchievement representation
        :type request: GameCenterAchievementV2CreateRequest

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementV2Response.parse_obj(json)

class GameCenterAchievementEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievements/{id}'

    @endpoint('/v2/gameCenterAchievements/{id}/versions')
    def versions(self) -> VersionsOfGameCenterAchievementEndpoint:
        return VersionsOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterAchievements/{id}/relationships/activity')
    def activity_linkage(self) -> ActivityLinkageOfGameCenterAchievementEndpoint:
        return ActivityLinkageOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterAchievements/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfGameCenterAchievementEndpoint:
        return VersionsLinkagesOfGameCenterAchievementEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]]=None) -> GameCenterAchievementEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_achievement_version: the fields to include for returned resources of type gameCenterAchievementVersions
        :type game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementEndpoint
        '''
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_achievement_version: self._set_fields('gameCenterAchievementVersions',game_center_achievement_version if type(game_center_achievement_version) is list else [game_center_achievement_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        ACTIVITY = 'activity'
        VERSIONS = 'versions'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, versions: int=None) -> GameCenterAchievementEndpoint:
        '''Number of included related resources to return.

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementEndpoint
        '''
        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterAchievementV2Response:
        '''Get the resource.

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementV2Response.parse_obj(json)

    def get_all(self) -> GameCenterAchievementV2Response:
        '''
        Get all resources.

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementV2Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementV2Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def update(self, request: GameCenterAchievementV2UpdateRequest) -> GameCenterAchievementV2Response:
        '''Modify the resource.

        :param request: GameCenterAchievement representation
        :type request: GameCenterAchievementV2UpdateRequest

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterAchievementV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterAchievementsEndpoint(Endpoint):
    path = '/v1/gameCenterAchievements'

    @deprecated
    def create(self, request: GameCenterAchievementCreateRequest) -> GameCenterAchievementResponse:
        '''Create the resource.

        :param request: GameCenterAchievement representation
        :type request: GameCenterAchievementCreateRequest

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementResponse.parse_obj(json)

class GameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}'

    @endpoint('/v1/gameCenterAchievements/{id}/groupAchievement')
    def group_achievement(self) -> GroupAchievementOfGameCenterAchievementEndpoint:
        return GroupAchievementOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievements/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterAchievementEndpoint:
        return LocalizationsOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievements/{id}/releases')
    def releases(self) -> ReleasesOfGameCenterAchievementEndpoint:
        return ReleasesOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievements/{id}/relationships/activity')
    def activity_linkage(self) -> ActivityLinkageOfGameCenterAchievementEndpoint:
        return ActivityLinkageOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievements/{id}/relationships/groupAchievement')
    def group_achievement_linkage(self) -> GroupAchievementLinkageOfGameCenterAchievementEndpoint:
        return GroupAchievementLinkageOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievements/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterAchievementEndpoint:
        return LocalizationsLinkagesOfGameCenterAchievementEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAchievements/{id}/relationships/releases')
    def releases_linkages(self) -> ReleasesLinkagesOfGameCenterAchievementEndpoint:
        return ReleasesLinkagesOfGameCenterAchievementEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None) -> GameCenterAchievementEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :param game_center_achievement_release: the fields to include for returned resources of type gameCenterAchievementReleases
        :type game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementEndpoint
        '''
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        if game_center_achievement_release: self._set_fields('gameCenterAchievementReleases',game_center_achievement_release if type(game_center_achievement_release) is list else [game_center_achievement_release])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GROUP_ACHIEVEMENT = 'groupAchievement'
        LOCALIZATIONS = 'localizations'
        RELEASES = 'releases'
        ACTIVITY = 'activity'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None, releases: int=None) -> GameCenterAchievementEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementEndpoint
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

    @deprecated
    def get_all(self) -> GameCenterAchievementResponse:
        '''
        Get all resources.

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    @deprecated
    def update(self, request: GameCenterAchievementUpdateRequest) -> GameCenterAchievementResponse:
        '''Modify the resource.

        :param request: GameCenterAchievement representation
        :type request: GameCenterAchievementUpdateRequest

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterAchievementResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class ActivityLinkageOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievements/{id}/relationships/activity'

    def update(self, request: GameCenterAchievementV2ActivityLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterAchievementV2ActivityLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class VersionsLinkagesOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievements/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfGameCenterAchievementEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfGameCenterAchievementEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterAchievementV2VersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterAchievementV2VersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementV2VersionsLinkagesResponse.parse_obj(json)

    def get_all(self) -> GameCenterAchievementV2VersionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: GameCenterAchievementV2VersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementV2VersionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementV2VersionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class VersionsOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievements/{id}/versions'

    def fields(self, *, game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None) -> VersionsOfGameCenterAchievementEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_version: the fields to include for returned resources of type gameCenterAchievementVersions
        :type game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterAchievementEndpoint
        '''
        if game_center_achievement_version: self._set_fields('gameCenterAchievementVersions',game_center_achievement_version if type(game_center_achievement_version) is list else [game_center_achievement_version])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        return self
        
    class Include(StringEnum):
        ACHIEVEMENT = 'achievement'
        LOCALIZATIONS = 'localizations'

    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfGameCenterAchievementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterAchievementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None) -> VersionsOfGameCenterAchievementEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterAchievementEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> GameCenterAchievementVersionsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterAchievementVersions
        :rtype: GameCenterAchievementVersionsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementVersionsV2Response.parse_obj(json)

    def get_all(self) -> GameCenterAchievementVersionsV2Response:
        '''
        Get all resources.

        :returns: List of GameCenterAchievementVersions
        :rtype: GameCenterAchievementVersionsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementVersionsV2Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementVersionsV2Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class ActivityLinkageOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}/relationships/activity'

    @deprecated
    def update(self, request: GameCenterAchievementActivityLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterAchievementActivityLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GroupAchievementLinkageOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}/relationships/groupAchievement'

    @deprecated
    def get(self) -> GameCenterAchievementGroupAchievementLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterAchievementGroupAchievementLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementGroupAchievementLinkageResponse.parse_obj(json)
    @deprecated
    def update(self, request: GameCenterAchievementGroupAchievementLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterAchievementGroupAchievementLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GroupAchievementOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}/groupAchievement'

    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None) -> GroupAchievementOfGameCenterAchievementEndpoint:
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
        :rtype: applaud.endpoints.GroupAchievementOfGameCenterAchievementEndpoint
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

    def include(self, relationship: Union[Include, list[Include]]) -> GroupAchievementOfGameCenterAchievementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GroupAchievementOfGameCenterAchievementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None, releases: int=None) -> GroupAchievementOfGameCenterAchievementEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GroupAchievementOfGameCenterAchievementEndpoint
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

    @deprecated
    def get_all(self) -> GameCenterAchievementResponse:
        '''
        Get all resources.

        :returns: Single GameCenterAchievement
        :rtype: GameCenterAchievementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class LocalizationsLinkagesOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterAchievementEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterAchievementEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterAchievementLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterAchievementLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationsLinkagesResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> GameCenterAchievementLocalizationsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: GameCenterAchievementLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementLocalizationsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementLocalizationsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class LocalizationsOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}/localizations'

    def fields(self, *, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None) -> LocalizationsOfGameCenterAchievementEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_localization: the fields to include for returned resources of type gameCenterAchievementLocalizations
        :type game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterAchievementEndpoint
        '''
        if game_center_achievement_localization: self._set_fields('gameCenterAchievementLocalizations',game_center_achievement_localization if type(game_center_achievement_localization) is list else [game_center_achievement_localization])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_ACHIEVEMENT = 'gameCenterAchievement'
        GAME_CENTER_ACHIEVEMENT_IMAGE = 'gameCenterAchievementImage'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterAchievementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterAchievementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterAchievementEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterAchievementEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterAchievementLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterAchievementLocalizations
        :rtype: GameCenterAchievementLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementLocalizationsResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> GameCenterAchievementLocalizationsResponse:
        '''
        Get all resources.

        :returns: List of GameCenterAchievementLocalizations
        :rtype: GameCenterAchievementLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementLocalizationsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementLocalizationsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class ReleasesLinkagesOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}/relationships/releases'

    def limit(self, number: int=None) -> ReleasesLinkagesOfGameCenterAchievementEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesLinkagesOfGameCenterAchievementEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterAchievementReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterAchievementReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementReleasesLinkagesResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> GameCenterAchievementReleasesLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: GameCenterAchievementReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementReleasesLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementReleasesLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class ReleasesOfGameCenterAchievementEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievements/{id}/releases'

    def fields(self, *, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None) -> ReleasesOfGameCenterAchievementEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_release: the fields to include for returned resources of type gameCenterAchievementReleases
        :type game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterAchievementEndpoint
        '''
        if game_center_achievement_release: self._set_fields('gameCenterAchievementReleases',game_center_achievement_release if type(game_center_achievement_release) is list else [game_center_achievement_release])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_ACHIEVEMENT = 'gameCenterAchievement'

    def filter(self, *, live: Union[str, list[str]]=None, game_center_detail: Union[str, list[str]]=None) -> ReleasesOfGameCenterAchievementEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param live: filter by attribute 'live'
        :type live: Union[str, list[str]] = None

        :param game_center_detail: filter by id(s) of related 'gameCenterDetail'
        :type game_center_detail: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterAchievementEndpoint
        '''
        if live: self._set_filter('live', live if type(live) is list else [live])
        
        if game_center_detail: self._set_filter('gameCenterDetail', game_center_detail if type(game_center_detail) is list else [game_center_detail])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ReleasesOfGameCenterAchievementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterAchievementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ReleasesOfGameCenterAchievementEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterAchievementEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterAchievementReleasesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterAchievementReleases
        :rtype: GameCenterAchievementReleasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementReleasesResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> GameCenterAchievementReleasesResponse:
        '''
        Get all resources.

        :returns: List of GameCenterAchievementReleases
        :rtype: GameCenterAchievementReleasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterAchievementReleasesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterAchievementReleasesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

