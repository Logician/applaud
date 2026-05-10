from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardSetMemberLocalizationsEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardSetMemberLocalizations'

    def fields(self, *, game_center_leaderboard_set_member_localization: Union[GameCenterLeaderboardSetMemberLocalizationField, list[GameCenterLeaderboardSetMemberLocalizationField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None) -> GameCenterLeaderboardSetMemberLocalizationsEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_member_localization: the fields to include for returned resources of type gameCenterLeaderboardSetMemberLocalizations
        :type game_center_leaderboard_set_member_localization: Union[GameCenterLeaderboardSetMemberLocalizationField, list[GameCenterLeaderboardSetMemberLocalizationField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetMemberLocalizationsEndpoint
        '''
        if game_center_leaderboard_set_member_localization: self._set_fields('gameCenterLeaderboardSetMemberLocalizations',game_center_leaderboard_set_member_localization if type(game_center_leaderboard_set_member_localization) is list else [game_center_leaderboard_set_member_localization])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD_SET = 'gameCenterLeaderboardSet'
        GAME_CENTER_LEADERBOARD = 'gameCenterLeaderboard'

    def filter(self, *, game_center_leaderboard_set: Union[str, list[str]], game_center_leaderboard: Union[str, list[str]]) -> GameCenterLeaderboardSetMemberLocalizationsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param game_center_leaderboard_set: filter by id(s) of related 'gameCenterLeaderboardSet'
        :type game_center_leaderboard_set: Union[str, list[str]]

        :param game_center_leaderboard: filter by id(s) of related 'gameCenterLeaderboard'
        :type game_center_leaderboard: Union[str, list[str]]

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetMemberLocalizationsEndpoint
        '''
        if game_center_leaderboard_set: self._set_filter('gameCenterLeaderboardSet', game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        
        if game_center_leaderboard: self._set_filter('gameCenterLeaderboard', game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetMemberLocalizationsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetMemberLocalizationsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> GameCenterLeaderboardSetMemberLocalizationsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetMemberLocalizationsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterLeaderboardSetMemberLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardSetMemberLocalizations
        :rtype: GameCenterLeaderboardSetMemberLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetMemberLocalizationsResponse.parse_obj(json)

    def get_all(self) -> GameCenterLeaderboardSetMemberLocalizationsResponse:
        '''
        Get all resources.

        :returns: List of GameCenterLeaderboardSetMemberLocalizations
        :rtype: GameCenterLeaderboardSetMemberLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterLeaderboardSetMemberLocalizationsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterLeaderboardSetMemberLocalizationsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def create(self, request: GameCenterLeaderboardSetMemberLocalizationCreateRequest) -> GameCenterLeaderboardSetMemberLocalizationResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardSetMemberLocalization representation
        :type request: GameCenterLeaderboardSetMemberLocalizationCreateRequest

        :returns: Single GameCenterLeaderboardSetMemberLocalization
        :rtype: GameCenterLeaderboardSetMemberLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetMemberLocalizationResponse.parse_obj(json)

class GameCenterLeaderboardSetMemberLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetMemberLocalizations/{id}'

    @endpoint('/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/gameCenterLeaderboard')
    def game_center_leaderboard(self) -> GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        return GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/gameCenterLeaderboardSet')
    def game_center_leaderboard_set(self) -> GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        return GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/relationships/gameCenterLeaderboard')
    def game_center_leaderboard_linkage(self) -> GameCenterLeaderboardLinkageOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        return GameCenterLeaderboardLinkageOfGameCenterLeaderboardSetMemberLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/relationships/gameCenterLeaderboardSet')
    def game_center_leaderboard_set_linkage(self) -> GameCenterLeaderboardSetLinkageOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        return GameCenterLeaderboardSetLinkageOfGameCenterLeaderboardSetMemberLocalizationEndpoint(self.id, self.session)
        
    def update(self, request: GameCenterLeaderboardSetMemberLocalizationUpdateRequest) -> GameCenterLeaderboardSetMemberLocalizationResponse:
        '''Modify the resource.

        :param request: GameCenterLeaderboardSetMemberLocalization representation
        :type request: GameCenterLeaderboardSetMemberLocalizationUpdateRequest

        :returns: Single GameCenterLeaderboardSetMemberLocalization
        :rtype: GameCenterLeaderboardSetMemberLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardSetMemberLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardLinkageOfGameCenterLeaderboardSetMemberLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/relationships/gameCenterLeaderboard'

    @deprecated
    def get(self) -> GameCenterLeaderboardSetMemberLocalizationGameCenterLeaderboardLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterLeaderboardSetMemberLocalizationGameCenterLeaderboardLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetMemberLocalizationGameCenterLeaderboardLinkageResponse.parse_obj(json)
class GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/gameCenterLeaderboard'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint
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

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_leaderboard_sets: int=None, localizations: int=None, releases: int=None) -> GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        '''Number of included related resources to return.

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardOfGameCenterLeaderboardSetMemberLocalizationEndpoint
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
    def get_all(self) -> GameCenterLeaderboardResponse:
        '''
        Get all resources.

        :returns: Single GameCenterLeaderboard
        :rtype: GameCenterLeaderboardResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterLeaderboardResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterLeaderboardResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class GameCenterLeaderboardSetLinkageOfGameCenterLeaderboardSetMemberLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/relationships/gameCenterLeaderboardSet'

    @deprecated
    def get(self) -> GameCenterLeaderboardSetMemberLocalizationGameCenterLeaderboardSetLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterLeaderboardSetMemberLocalizationGameCenterLeaderboardSetLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetMemberLocalizationGameCenterLeaderboardSetLinkageResponse.parse_obj(json)
class GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/gameCenterLeaderboardSet'

    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None) -> GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint
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

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None, game_center_leaderboards: int=None, releases: int=None) -> GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetOfGameCenterLeaderboardSetMemberLocalizationEndpoint
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

    @deprecated
    def get_all(self) -> GameCenterLeaderboardSetResponse:
        '''
        Get all resources.

        :returns: Single GameCenterLeaderboardSet
        :rtype: GameCenterLeaderboardSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterLeaderboardSetResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterLeaderboardSetResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

