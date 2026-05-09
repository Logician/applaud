from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterActivitiesEndpoint(Endpoint):
    path = '/v1/gameCenterActivities'

    def create(self, request: GameCenterActivityCreateRequest) -> GameCenterActivityResponse:
        '''Create the resource.

        :param request: GameCenterActivity representation
        :type request: GameCenterActivityCreateRequest

        :returns: Single GameCenterActivity
        :rtype: GameCenterActivityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterActivityResponse.parse_obj(json)

class GameCenterActivityEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivities/{id}'

    @endpoint('/v1/gameCenterActivities/{id}/versions')
    def versions(self) -> VersionsOfGameCenterActivityEndpoint:
        return VersionsOfGameCenterActivityEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivities/{id}/relationships/achievements')
    def achievements_linkages(self) -> AchievementsLinkagesOfGameCenterActivityEndpoint:
        return AchievementsLinkagesOfGameCenterActivityEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivities/{id}/relationships/achievementsV2')
    def achievements_v2_linkage(self) -> AchievementsV2LinkageOfGameCenterActivityEndpoint:
        return AchievementsV2LinkageOfGameCenterActivityEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivities/{id}/relationships/leaderboards')
    def leaderboards_linkages(self) -> LeaderboardsLinkagesOfGameCenterActivityEndpoint:
        return LeaderboardsLinkagesOfGameCenterActivityEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivities/{id}/relationships/leaderboardsV2')
    def leaderboards_v2_linkage(self) -> LeaderboardsV2LinkageOfGameCenterActivityEndpoint:
        return LeaderboardsV2LinkageOfGameCenterActivityEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterActivities/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfGameCenterActivityEndpoint:
        return VersionsLinkagesOfGameCenterActivityEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None) -> GameCenterActivityEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_activity_version: the fields to include for returned resources of type gameCenterActivityVersions
        :type game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityEndpoint
        '''
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_activity_version: self._set_fields('gameCenterActivityVersions',game_center_activity_version if type(game_center_activity_version) is list else [game_center_activity_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        ACHIEVEMENTS = 'achievements'
        ACHIEVEMENTS_V2 = 'achievementsV2'
        LEADERBOARDS = 'leaderboards'
        LEADERBOARDS_V2 = 'leaderboardsV2'
        VERSIONS = 'versions'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterActivityEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, achievements: int=None, achievements_v2: int=None, leaderboards: int=None, leaderboards_v2: int=None, versions: int=None) -> GameCenterActivityEndpoint:
        '''Number of included related resources to return.

        :param achievements: maximum number of related achievements returned (when they are included). The maximum limit is 50
        :type achievements: int = None

        :param achievements_v2: maximum number of related achievementsV2 returned (when they are included). The maximum limit is 50
        :type achievements_v2: int = None

        :param leaderboards: maximum number of related leaderboards returned (when they are included). The maximum limit is 50
        :type leaderboards: int = None

        :param leaderboards_v2: maximum number of related leaderboardsV2 returned (when they are included). The maximum limit is 50
        :type leaderboards_v2: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityEndpoint
        '''
        if achievements and achievements > 50:
            raise ValueError(f'The maximum limit of achievements is 50')
        if achievements: self._set_limit(achievements, 'achievements')

        if achievements_v2 and achievements_v2 > 50:
            raise ValueError(f'The maximum limit of achievements_v2 is 50')
        if achievements_v2: self._set_limit(achievements_v2, 'achievementsV2')

        if leaderboards and leaderboards > 50:
            raise ValueError(f'The maximum limit of leaderboards is 50')
        if leaderboards: self._set_limit(leaderboards, 'leaderboards')

        if leaderboards_v2 and leaderboards_v2 > 50:
            raise ValueError(f'The maximum limit of leaderboards_v2 is 50')
        if leaderboards_v2: self._set_limit(leaderboards_v2, 'leaderboardsV2')

        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterActivityResponse:
        '''Get the resource.

        :returns: Single GameCenterActivity
        :rtype: GameCenterActivityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityResponse.parse_obj(json)

    def update(self, request: GameCenterActivityUpdateRequest) -> GameCenterActivityResponse:
        '''Modify the resource.

        :param request: GameCenterActivity representation
        :type request: GameCenterActivityUpdateRequest

        :returns: Single GameCenterActivity
        :rtype: GameCenterActivityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterActivityResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AchievementsLinkagesOfGameCenterActivityEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivities/{id}/relationships/achievements'

    @deprecated
    def create(self, request: GameCenterActivityAchievementsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityAchievementsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    @deprecated
    def delete(self, request: GameCenterActivityAchievementsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityAchievementsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class AchievementsV2LinkageOfGameCenterActivityEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivities/{id}/relationships/achievementsV2'

    def create(self, request: GameCenterActivityAchievementsV2LinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityAchievementsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: GameCenterActivityAchievementsV2LinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityAchievementsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class LeaderboardsLinkagesOfGameCenterActivityEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivities/{id}/relationships/leaderboards'

    @deprecated
    def create(self, request: GameCenterActivityLeaderboardsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    @deprecated
    def delete(self, request: GameCenterActivityLeaderboardsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class LeaderboardsV2LinkageOfGameCenterActivityEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivities/{id}/relationships/leaderboardsV2'

    def create(self, request: GameCenterActivityLeaderboardsV2LinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityLeaderboardsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: GameCenterActivityLeaderboardsV2LinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterActivityLeaderboardsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class VersionsLinkagesOfGameCenterActivityEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivities/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfGameCenterActivityEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfGameCenterActivityEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterActivityVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterActivityVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityVersionsLinkagesResponse.parse_obj(json)

class VersionsOfGameCenterActivityEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivities/{id}/versions'

    def fields(self, *, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]]=None, game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]]=None, game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]]=None) -> VersionsOfGameCenterActivityEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_version: the fields to include for returned resources of type gameCenterActivityVersions
        :type game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_activity_localization: the fields to include for returned resources of type gameCenterActivityLocalizations
        :type game_center_activity_localization: Union[GameCenterActivityLocalizationField, list[GameCenterActivityLocalizationField]] = None

        :param game_center_activity_image: the fields to include for returned resources of type gameCenterActivityImages
        :type game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]] = None

        :param game_center_activity_version_release: the fields to include for returned resources of type gameCenterActivityVersionReleases
        :type game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterActivityEndpoint
        '''
        if game_center_activity_version: self._set_fields('gameCenterActivityVersions',game_center_activity_version if type(game_center_activity_version) is list else [game_center_activity_version])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_activity_localization: self._set_fields('gameCenterActivityLocalizations',game_center_activity_localization if type(game_center_activity_localization) is list else [game_center_activity_localization])
        if game_center_activity_image: self._set_fields('gameCenterActivityImages',game_center_activity_image if type(game_center_activity_image) is list else [game_center_activity_image])
        if game_center_activity_version_release: self._set_fields('gameCenterActivityVersionReleases',game_center_activity_version_release if type(game_center_activity_version_release) is list else [game_center_activity_version_release])
        return self
        
    class Include(StringEnum):
        ACTIVITY = 'activity'
        LOCALIZATIONS = 'localizations'
        DEFAULT_IMAGE = 'defaultImage'
        RELEASES = 'releases'

    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfGameCenterActivityEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterActivityEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None, releases: int=None) -> VersionsOfGameCenterActivityEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterActivityEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    def get(self) -> GameCenterActivityVersionsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterActivityVersions
        :rtype: GameCenterActivityVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityVersionsResponse.parse_obj(json)

