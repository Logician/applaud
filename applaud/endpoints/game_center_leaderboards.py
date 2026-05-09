from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardsEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboards'

    @deprecated
    def create(self, request: GameCenterLeaderboardCreateRequest) -> GameCenterLeaderboardResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboard representation
        :type request: GameCenterLeaderboardCreateRequest

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardResponse.parse_obj(json)

class GameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}'

    @endpoint('/v1/gameCenterLeaderboards/{id}/groupLeaderboard')
    def group_leaderboard(self) -> GroupLeaderboardOfGameCenterLeaderboardEndpoint:
        return GroupLeaderboardOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboards/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterLeaderboardEndpoint:
        return LocalizationsOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboards/{id}/releases')
    def releases(self) -> ReleasesOfGameCenterLeaderboardEndpoint:
        return ReleasesOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboards/{id}/relationships/activity')
    def activity_linkage(self) -> ActivityLinkageOfGameCenterLeaderboardEndpoint:
        return ActivityLinkageOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboards/{id}/relationships/challenge')
    def challenge_linkage(self) -> ChallengeLinkageOfGameCenterLeaderboardEndpoint:
        return ChallengeLinkageOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboards/{id}/relationships/groupLeaderboard')
    def group_leaderboard_linkage(self) -> GroupLeaderboardLinkageOfGameCenterLeaderboardEndpoint:
        return GroupLeaderboardLinkageOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboards/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterLeaderboardEndpoint:
        return LocalizationsLinkagesOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboards/{id}/relationships/releases')
    def releases_linkages(self) -> ReleasesLinkagesOfGameCenterLeaderboardEndpoint:
        return ReleasesLinkagesOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None) -> GameCenterLeaderboardEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :param game_center_leaderboard_release: the fields to include for returned resources of type gameCenterLeaderboardReleases
        :type game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        if game_center_leaderboard_release: self._set_fields('gameCenterLeaderboardReleases',game_center_leaderboard_release if type(game_center_leaderboard_release) is list else [game_center_leaderboard_release])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GROUP_LEADERBOARD = 'groupLeaderboard'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        LOCALIZATIONS = 'localizations'
        RELEASES = 'releases'
        ACTIVITY = 'activity'
        CHALLENGE = 'challenge'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_leaderboard_sets: int=None, localizations: int=None, releases: int=None) -> GameCenterLeaderboardEndpoint:
        '''Number of included related resources to return.

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterLeaderboardUpdateRequest) -> GameCenterLeaderboardResponse:
        '''Modify the resource.

        :param request: GameCenterLeaderboard representation
        :type request: GameCenterLeaderboardUpdateRequest

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardsEndpoint(Endpoint):
    path = '/v2/gameCenterLeaderboards'

    def create(self, request: GameCenterLeaderboardV2CreateRequest) -> GameCenterLeaderboardV2Response:
        '''Create the resource.

        :param request: GameCenterLeaderboard representation
        :type request: GameCenterLeaderboardV2CreateRequest

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardV2Response.parse_obj(json)

class GameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboards/{id}'

    @endpoint('/v2/gameCenterLeaderboards/{id}/versions')
    def versions(self) -> VersionsOfGameCenterLeaderboardEndpoint:
        return VersionsOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboards/{id}/relationships/activity')
    def activity_linkage(self) -> ActivityLinkageOfGameCenterLeaderboardEndpoint:
        return ActivityLinkageOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboards/{id}/relationships/challenge')
    def challenge_linkage(self) -> ChallengeLinkageOfGameCenterLeaderboardEndpoint:
        return ChallengeLinkageOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboards/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfGameCenterLeaderboardEndpoint:
        return VersionsLinkagesOfGameCenterLeaderboardEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None) -> GameCenterLeaderboardEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_version: the fields to include for returned resources of type gameCenterLeaderboardVersions
        :type game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_version: self._set_fields('gameCenterLeaderboardVersions',game_center_leaderboard_version if type(game_center_leaderboard_version) is list else [game_center_leaderboard_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        ACTIVITY = 'activity'
        CHALLENGE = 'challenge'
        VERSIONS = 'versions'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_leaderboard_sets: int=None, versions: int=None) -> GameCenterLeaderboardEndpoint:
        '''Number of included related resources to return.

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterLeaderboardV2Response:
        '''Get the resource.

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardV2Response.parse_obj(json)

    def update(self, request: GameCenterLeaderboardV2UpdateRequest) -> GameCenterLeaderboardV2Response:
        '''Modify the resource.

        :param request: GameCenterLeaderboard representation
        :type request: GameCenterLeaderboardV2UpdateRequest

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class ActivityLinkageOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/relationships/activity'

    @deprecated
    def update(self, request: GameCenterLeaderboardActivityLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterLeaderboardActivityLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class ChallengeLinkageOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/relationships/challenge'

    @deprecated
    def update(self, request: GameCenterLeaderboardChallengeLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterLeaderboardChallengeLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GroupLeaderboardLinkageOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/relationships/groupLeaderboard'

    @deprecated
    def get(self) -> GameCenterLeaderboardGroupLeaderboardLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterLeaderboardGroupLeaderboardLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardGroupLeaderboardLinkageResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterLeaderboardGroupLeaderboardLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterLeaderboardGroupLeaderboardLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GroupLeaderboardOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/groupLeaderboard'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GroupLeaderboardOfGameCenterLeaderboardEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :param game_center_leaderboard_release: the fields to include for returned resources of type gameCenterLeaderboardReleases
        :type game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :returns: self
        :rtype: applaud.endpoints.GroupLeaderboardOfGameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        if game_center_leaderboard_release: self._set_fields('gameCenterLeaderboardReleases',game_center_leaderboard_release if type(game_center_leaderboard_release) is list else [game_center_leaderboard_release])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GROUP_LEADERBOARD = 'groupLeaderboard'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        LOCALIZATIONS = 'localizations'
        RELEASES = 'releases'
        ACTIVITY = 'activity'
        CHALLENGE = 'challenge'

    def include(self, relationship: Union[Include, list[Include]]) -> GroupLeaderboardOfGameCenterLeaderboardEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GroupLeaderboardOfGameCenterLeaderboardEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_leaderboard_sets: int=None, localizations: int=None, releases: int=None) -> GroupLeaderboardOfGameCenterLeaderboardEndpoint:
        '''Number of included related resources to return.

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GroupLeaderboardOfGameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardResponse.parse_obj(json)

class LocalizationsLinkagesOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterLeaderboardEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterLeaderboardEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardLocalizationsLinkagesResponse.parse_obj(json)

class LocalizationsOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/localizations'

    def fields(self, *, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]]=None) -> LocalizationsOfGameCenterLeaderboardEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_image: the fields to include for returned resources of type gameCenterLeaderboardImages
        :type game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_image: self._set_fields('gameCenterLeaderboardImages',game_center_leaderboard_image if type(game_center_leaderboard_image) is list else [game_center_leaderboard_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD = 'gameCenterLeaderboard'
        GAME_CENTER_LEADERBOARD_IMAGE = 'gameCenterLeaderboardImage'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterLeaderboardEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterLeaderboardEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardLocalizations
        :rtype: GameCenterLeaderboardLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardLocalizationsResponse.parse_obj(json)

class ReleasesLinkagesOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/relationships/releases'

    def limit(self, number: int=None) -> ReleasesLinkagesOfGameCenterLeaderboardEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesLinkagesOfGameCenterLeaderboardEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardReleasesLinkagesResponse.parse_obj(json)

class ReleasesOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboards/{id}/releases'

    def fields(self, *, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None) -> ReleasesOfGameCenterLeaderboardEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_release: the fields to include for returned resources of type gameCenterLeaderboardReleases
        :type game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard_release: self._set_fields('gameCenterLeaderboardReleases',game_center_leaderboard_release if type(game_center_leaderboard_release) is list else [game_center_leaderboard_release])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_LEADERBOARD = 'gameCenterLeaderboard'

    def filter(self, *, live: Union[str, list[str]]=None, game_center_detail: Union[str, list[str]]=None) -> ReleasesOfGameCenterLeaderboardEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param live: filter by attribute 'live'
        :type live: Union[str, list[str]] = None

        :param game_center_detail: filter by id(s) of related 'gameCenterDetail'
        :type game_center_detail: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardEndpoint
        '''
        if live: self._set_filter('live', live if type(live) is list else [live])
        
        if game_center_detail: self._set_filter('gameCenterDetail', game_center_detail if type(game_center_detail) is list else [game_center_detail])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ReleasesOfGameCenterLeaderboardEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ReleasesOfGameCenterLeaderboardEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardReleasesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardReleases
        :rtype: GameCenterLeaderboardReleasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardReleasesResponse.parse_obj(json)

class ActivityLinkageOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboards/{id}/relationships/activity'

    def update(self, request: GameCenterLeaderboardV2ActivityLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterLeaderboardV2ActivityLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class ChallengeLinkageOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboards/{id}/relationships/challenge'

    def update(self, request: GameCenterLeaderboardV2ChallengeLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterLeaderboardV2ChallengeLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class VersionsLinkagesOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboards/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfGameCenterLeaderboardEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfGameCenterLeaderboardEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardV2VersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardV2VersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardV2VersionsLinkagesResponse.parse_obj(json)

class VersionsOfGameCenterLeaderboardEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboards/{id}/versions'

    def fields(self, *, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None) -> VersionsOfGameCenterLeaderboardEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_version: the fields to include for returned resources of type gameCenterLeaderboardVersions
        :type game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_localization: the fields to include for returned resources of type gameCenterLeaderboardLocalizations
        :type game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterLeaderboardEndpoint
        '''
        if game_center_leaderboard_version: self._set_fields('gameCenterLeaderboardVersions',game_center_leaderboard_version if type(game_center_leaderboard_version) is list else [game_center_leaderboard_version])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_localization: self._set_fields('gameCenterLeaderboardLocalizations',game_center_leaderboard_localization if type(game_center_leaderboard_localization) is list else [game_center_leaderboard_localization])
        return self
        
    class Include(StringEnum):
        LEADERBOARD = 'leaderboard'
        LOCALIZATIONS = 'localizations'

    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfGameCenterLeaderboardEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterLeaderboardEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None) -> VersionsOfGameCenterLeaderboardEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterLeaderboardEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> GameCenterLeaderboardVersionsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardVersions
        :rtype: GameCenterLeaderboardVersionsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardVersionsV2Response.parse_obj(json)

