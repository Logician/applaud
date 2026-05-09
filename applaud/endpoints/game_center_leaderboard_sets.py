from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardSetsEndpoint(Endpoint):
    path = '/v2/gameCenterLeaderboardSets'

    def create(self, request: GameCenterLeaderboardSetV2CreateRequest) -> GameCenterLeaderboardSetV2Response:
        '''Create the resource.

        :param request: GameCenterLeaderboardSet representation
        :type request: GameCenterLeaderboardSetV2CreateRequest

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetV2Response.parse_obj(json)

class GameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSets/{id}'

    @endpoint('/v2/gameCenterLeaderboardSets/{id}/gameCenterLeaderboards')
    def game_center_leaderboards(self) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        return GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboardSets/{id}/versions')
    def versions(self) -> VersionsOfGameCenterLeaderboardSetEndpoint:
        return VersionsOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboardSets/{id}/relationships/gameCenterLeaderboards')
    def game_center_leaderboards_linkages(self) -> GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint:
        return GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v2/gameCenterLeaderboardSets/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfGameCenterLeaderboardSetEndpoint:
        return VersionsLinkagesOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]]=None) -> GameCenterLeaderboardSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set_version: the fields to include for returned resources of type gameCenterLeaderboardSetVersions
        :type game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set_version: self._set_fields('gameCenterLeaderboardSetVersions',game_center_leaderboard_set_version if type(game_center_leaderboard_set_version) is list else [game_center_leaderboard_set_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        VERSIONS = 'versions'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_leaderboards: int=None, versions: int=None) -> GameCenterLeaderboardSetEndpoint:
        '''Number of included related resources to return.

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterLeaderboardSetV2Response:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetV2Response.parse_obj(json)

    def update(self, request: GameCenterLeaderboardSetV2UpdateRequest) -> GameCenterLeaderboardSetV2Response:
        '''Modify the resource.

        :param request: GameCenterLeaderboardSet representation
        :type request: GameCenterLeaderboardSetV2UpdateRequest

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardSetV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardSetsEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardSets'

    @deprecated
    def create(self, request: GameCenterLeaderboardSetCreateRequest) -> GameCenterLeaderboardSetResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardSet representation
        :type request: GameCenterLeaderboardSetCreateRequest

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetResponse.parse_obj(json)

class GameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}'

    @endpoint('/v1/gameCenterLeaderboardSets/{id}/gameCenterLeaderboards')
    def game_center_leaderboards(self) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        return GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSets/{id}/groupLeaderboardSet')
    def group_leaderboard_set(self) -> GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint:
        return GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSets/{id}/localizations')
    def localizations(self) -> LocalizationsOfGameCenterLeaderboardSetEndpoint:
        return LocalizationsOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSets/{id}/releases')
    def releases(self) -> ReleasesOfGameCenterLeaderboardSetEndpoint:
        return ReleasesOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSets/{id}/relationships/gameCenterLeaderboards')
    def game_center_leaderboards_linkages(self) -> GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint:
        return GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSets/{id}/relationships/groupLeaderboardSet')
    def group_leaderboard_set_linkage(self) -> GroupLeaderboardSetLinkageOfGameCenterLeaderboardSetEndpoint:
        return GroupLeaderboardSetLinkageOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSets/{id}/relationships/localizations')
    def localizations_linkages(self) -> LocalizationsLinkagesOfGameCenterLeaderboardSetEndpoint:
        return LocalizationsLinkagesOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSets/{id}/relationships/releases')
    def releases_linkages(self) -> ReleasesLinkagesOfGameCenterLeaderboardSetEndpoint:
        return ReleasesLinkagesOfGameCenterLeaderboardSetEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None) -> GameCenterLeaderboardSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set_release: the fields to include for returned resources of type gameCenterLeaderboardSetReleases
        :type game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set_release: self._set_fields('gameCenterLeaderboardSetReleases',game_center_leaderboard_set_release if type(game_center_leaderboard_set_release) is list else [game_center_leaderboard_set_release])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GROUP_LEADERBOARD_SET = 'groupLeaderboardSet'
        LOCALIZATIONS = 'localizations'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        RELEASES = 'releases'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_leaderboards: int=None, localizations: int=None, releases: int=None) -> GameCenterLeaderboardSetEndpoint:
        '''Number of included related resources to return.

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardSetResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterLeaderboardSetUpdateRequest) -> GameCenterLeaderboardSetResponse:
        '''Modify the resource.

        :param request: GameCenterLeaderboardSet representation
        :type request: GameCenterLeaderboardSetUpdateRequest

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardSetResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSets/{id}/relationships/gameCenterLeaderboards'

    def limit(self, number: int=None) -> GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesResponse.parse_obj(json)

    def create(self, request: GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def update(self, request: GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

    def delete(self, request: GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSets/{id}/gameCenterLeaderboards'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :param game_center_leaderboard_version: the fields to include for returned resources of type gameCenterLeaderboardVersions
        :type game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        if game_center_leaderboard_version: self._set_fields('gameCenterLeaderboardVersions',game_center_leaderboard_version if type(game_center_leaderboard_version) is list else [game_center_leaderboard_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        ACTIVITY = 'activity'
        CHALLENGE = 'challenge'
        VERSIONS = 'versions'

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboard_sets: int=None, versions: int=None) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterLeaderboardsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboards
        :rtype: GameCenterLeaderboardsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardsV2Response.parse_obj(json)

class VersionsLinkagesOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSets/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardSetV2VersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardSetV2VersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetV2VersionsLinkagesResponse.parse_obj(json)

class VersionsOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSets/{id}/versions'

    def fields(self, *, game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None) -> VersionsOfGameCenterLeaderboardSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_version: the fields to include for returned resources of type gameCenterLeaderboardSetVersions
        :type game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboard_set_version: self._set_fields('gameCenterLeaderboardSetVersions',game_center_leaderboard_set_version if type(game_center_leaderboard_set_version) is list else [game_center_leaderboard_set_version])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        return self
        
    class Include(StringEnum):
        LEADERBOARD_SET = 'leaderboardSet'
        LOCALIZATIONS = 'localizations'

    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfGameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None) -> VersionsOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> GameCenterLeaderboardSetVersionsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardSetVersions
        :rtype: GameCenterLeaderboardSetVersionsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetVersionsV2Response.parse_obj(json)

class GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/relationships/gameCenterLeaderboards'

    def limit(self, number: int=None) -> GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsLinkagesOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesResponse.parse_obj(json)

    @deprecated
    def create(self, request: GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    @deprecated
    def update(self, request: GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

    @deprecated
    def delete(self, request: GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/gameCenterLeaderboards'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboard_sets: int=None, localizations: int=None, releases: int=None) -> GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
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
    def get(self) -> GameCenterLeaderboardsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboards
        :rtype: GameCenterLeaderboardsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardsResponse.parse_obj(json)

class GroupLeaderboardSetLinkageOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/relationships/groupLeaderboardSet'

    @deprecated
    def get(self) -> GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterLeaderboardSetGroupLeaderboardSetLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterLeaderboardSetGroupLeaderboardSetLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/groupLeaderboardSet'

    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None) -> GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set_release: the fields to include for returned resources of type gameCenterLeaderboardSetReleases
        :type game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set_release: self._set_fields('gameCenterLeaderboardSetReleases',game_center_leaderboard_set_release if type(game_center_leaderboard_set_release) is list else [game_center_leaderboard_set_release])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GROUP_LEADERBOARD_SET = 'groupLeaderboardSet'
        LOCALIZATIONS = 'localizations'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        RELEASES = 'releases'

    def include(self, relationship: Union[Include, list[Include]]) -> GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None, game_center_leaderboards: int=None, releases: int=None) -> GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GroupLeaderboardSetOfGameCenterLeaderboardSetEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if releases and releases > 50:
            raise ValueError(f'The maximum limit of releases is 50')
        if releases: self._set_limit(releases, 'releases')

        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardSetResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetResponse.parse_obj(json)

class LocalizationsLinkagesOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/relationships/localizations'

    def limit(self, number: int=None) -> LocalizationsLinkagesOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsLinkagesOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardSetLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardSetLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetLocalizationsLinkagesResponse.parse_obj(json)

class LocalizationsOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/localizations'

    def fields(self, *, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None) -> LocalizationsOfGameCenterLeaderboardSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_localization: the fields to include for returned resources of type gameCenterLeaderboardSetLocalizations
        :type game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboard_set_localization: self._set_fields('gameCenterLeaderboardSetLocalizations',game_center_leaderboard_set_localization if type(game_center_leaderboard_set_localization) is list else [game_center_leaderboard_set_localization])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD_SET = 'gameCenterLeaderboardSet'
        GAME_CENTER_LEADERBOARD_SET_IMAGE = 'gameCenterLeaderboardSetImage'

    def include(self, relationship: Union[Include, list[Include]]) -> LocalizationsOfGameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LocalizationsOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LocalizationsOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardSetLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardSetLocalizations
        :rtype: GameCenterLeaderboardSetLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetLocalizationsResponse.parse_obj(json)

class ReleasesLinkagesOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/relationships/releases'

    def limit(self, number: int=None) -> ReleasesLinkagesOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesLinkagesOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardSetReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterLeaderboardSetReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetReleasesLinkagesResponse.parse_obj(json)

class ReleasesOfGameCenterLeaderboardSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSets/{id}/releases'

    def fields(self, *, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None) -> ReleasesOfGameCenterLeaderboardSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_release: the fields to include for returned resources of type gameCenterLeaderboardSetReleases
        :type game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardSetEndpoint
        '''
        if game_center_leaderboard_set_release: self._set_fields('gameCenterLeaderboardSetReleases',game_center_leaderboard_set_release if type(game_center_leaderboard_set_release) is list else [game_center_leaderboard_set_release])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_LEADERBOARD_SET = 'gameCenterLeaderboardSet'

    def filter(self, *, live: Union[str, list[str]]=None, game_center_detail: Union[str, list[str]]=None) -> ReleasesOfGameCenterLeaderboardSetEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param live: filter by attribute 'live'
        :type live: Union[str, list[str]] = None

        :param game_center_detail: filter by id(s) of related 'gameCenterDetail'
        :type game_center_detail: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardSetEndpoint
        '''
        if live: self._set_filter('live', live if type(live) is list else [live])
        
        if game_center_detail: self._set_filter('gameCenterDetail', game_center_detail if type(game_center_detail) is list else [game_center_detail])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ReleasesOfGameCenterLeaderboardSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ReleasesOfGameCenterLeaderboardSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleasesOfGameCenterLeaderboardSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterLeaderboardSetReleasesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardSetReleases
        :rtype: GameCenterLeaderboardSetReleasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetReleasesResponse.parse_obj(json)

