from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterGroupsEndpoint(Endpoint):
    path = '/v1/gameCenterGroups'

    def fields(self, *, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GameCenterGroupsEndpoint:
        '''Fields to return for included related types.

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupsEndpoint
        '''
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAILS = 'gameCenterDetails'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        GAME_CENTER_LEADERBOARDS_V2 = 'gameCenterLeaderboardsV2'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        GAME_CENTER_LEADERBOARD_SETS_V2 = 'gameCenterLeaderboardSetsV2'
        GAME_CENTER_ACHIEVEMENTS = 'gameCenterAchievements'
        GAME_CENTER_ACHIEVEMENTS_V2 = 'gameCenterAchievementsV2'
        GAME_CENTER_ACTIVITIES = 'gameCenterActivities'
        GAME_CENTER_CHALLENGES = 'gameCenterChallenges'

    def filter(self, *, game_center_details: Union[str, list[str]]=None) -> GameCenterGroupsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param game_center_details: filter by id(s) of related 'gameCenterDetails'
        :type game_center_details: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupsEndpoint
        '''
        if game_center_details: self._set_filter('gameCenterDetails', game_center_details if type(game_center_details) is list else [game_center_details])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterGroupsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_achievements: int=None, game_center_achievements_v2: int=None, game_center_activities: int=None, game_center_challenges: int=None, game_center_details: int=None, game_center_leaderboard_sets: int=None, game_center_leaderboard_sets_v2: int=None, game_center_leaderboards: int=None, game_center_leaderboards_v2: int=None) -> GameCenterGroupsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_achievements: maximum number of related gameCenterAchievements returned (when they are included). The maximum limit is 50
        :type game_center_achievements: int = None

        :param game_center_achievements_v2: maximum number of related gameCenterAchievementsV2 returned (when they are included). The maximum limit is 50
        :type game_center_achievements_v2: int = None

        :param game_center_activities: maximum number of related gameCenterActivities returned (when they are included). The maximum limit is 50
        :type game_center_activities: int = None

        :param game_center_challenges: maximum number of related gameCenterChallenges returned (when they are included). The maximum limit is 50
        :type game_center_challenges: int = None

        :param game_center_details: maximum number of related gameCenterDetails returned (when they are included). The maximum limit is 50
        :type game_center_details: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param game_center_leaderboard_sets_v2: maximum number of related gameCenterLeaderboardSetsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets_v2: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param game_center_leaderboards_v2: maximum number of related gameCenterLeaderboardsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards_v2: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if game_center_achievements and game_center_achievements > 50:
            raise ValueError(f'The maximum limit of game_center_achievements is 50')
        if game_center_achievements: self._set_limit(game_center_achievements, 'gameCenterAchievements')

        if game_center_achievements_v2 and game_center_achievements_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_achievements_v2 is 50')
        if game_center_achievements_v2: self._set_limit(game_center_achievements_v2, 'gameCenterAchievementsV2')

        if game_center_activities and game_center_activities > 50:
            raise ValueError(f'The maximum limit of game_center_activities is 50')
        if game_center_activities: self._set_limit(game_center_activities, 'gameCenterActivities')

        if game_center_challenges and game_center_challenges > 50:
            raise ValueError(f'The maximum limit of game_center_challenges is 50')
        if game_center_challenges: self._set_limit(game_center_challenges, 'gameCenterChallenges')

        if game_center_details and game_center_details > 50:
            raise ValueError(f'The maximum limit of game_center_details is 50')
        if game_center_details: self._set_limit(game_center_details, 'gameCenterDetails')

        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if game_center_leaderboard_sets_v2 and game_center_leaderboard_sets_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets_v2 is 50')
        if game_center_leaderboard_sets_v2: self._set_limit(game_center_leaderboard_sets_v2, 'gameCenterLeaderboardSetsV2')

        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if game_center_leaderboards_v2 and game_center_leaderboards_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards_v2 is 50')
        if game_center_leaderboards_v2: self._set_limit(game_center_leaderboards_v2, 'gameCenterLeaderboardsV2')

        return self

    def get(self) -> GameCenterGroupsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterGroups
        :rtype: GameCenterGroupsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupsResponse.parse_obj(json)

    def create(self, request: GameCenterGroupCreateRequest) -> GameCenterGroupResponse:
        '''Create the resource.

        :param request: GameCenterGroup representation
        :type request: GameCenterGroupCreateRequest

        :returns: Single GameCenterGroup
        :rtype: GameCenterGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterGroupResponse.parse_obj(json)

class GameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}'

    @endpoint('/v1/gameCenterGroups/{id}/gameCenterAchievements')
    def game_center_achievements(self) -> GameCenterAchievementsOfGameCenterGroupEndpoint:
        return GameCenterAchievementsOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterAchievementsV2')
    def game_center_achievements_v2(self) -> GameCenterAchievementsV2OfGameCenterGroupEndpoint:
        return GameCenterAchievementsV2OfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterActivities')
    def game_center_activities(self) -> GameCenterActivitiesOfGameCenterGroupEndpoint:
        return GameCenterActivitiesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterChallenges')
    def game_center_challenges(self) -> GameCenterChallengesOfGameCenterGroupEndpoint:
        return GameCenterChallengesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterDetails')
    def game_center_details(self) -> GameCenterDetailsOfGameCenterGroupEndpoint:
        return GameCenterDetailsOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterLeaderboardSets')
    def game_center_leaderboard_sets(self) -> GameCenterLeaderboardSetsOfGameCenterGroupEndpoint:
        return GameCenterLeaderboardSetsOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterLeaderboardSetsV2')
    def game_center_leaderboard_sets_v2(self) -> GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint:
        return GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterLeaderboards')
    def game_center_leaderboards(self) -> GameCenterLeaderboardsOfGameCenterGroupEndpoint:
        return GameCenterLeaderboardsOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/gameCenterLeaderboardsV2')
    def game_center_leaderboards_v2(self) -> GameCenterLeaderboardsV2OfGameCenterGroupEndpoint:
        return GameCenterLeaderboardsV2OfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterAchievements')
    def game_center_achievements_linkages(self) -> GameCenterAchievementsLinkagesOfGameCenterGroupEndpoint:
        return GameCenterAchievementsLinkagesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterAchievementsV2')
    def game_center_achievements_v2_linkage(self) -> GameCenterAchievementsV2LinkageOfGameCenterGroupEndpoint:
        return GameCenterAchievementsV2LinkageOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterActivities')
    def game_center_activities_linkages(self) -> GameCenterActivitiesLinkagesOfGameCenterGroupEndpoint:
        return GameCenterActivitiesLinkagesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterChallenges')
    def game_center_challenges_linkages(self) -> GameCenterChallengesLinkagesOfGameCenterGroupEndpoint:
        return GameCenterChallengesLinkagesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterDetails')
    def game_center_details_linkages(self) -> GameCenterDetailsLinkagesOfGameCenterGroupEndpoint:
        return GameCenterDetailsLinkagesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboardSets')
    def game_center_leaderboard_sets_linkages(self) -> GameCenterLeaderboardSetsLinkagesOfGameCenterGroupEndpoint:
        return GameCenterLeaderboardSetsLinkagesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboardSetsV2')
    def game_center_leaderboard_sets_v2_linkage(self) -> GameCenterLeaderboardSetsV2LinkageOfGameCenterGroupEndpoint:
        return GameCenterLeaderboardSetsV2LinkageOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboards')
    def game_center_leaderboards_linkages(self) -> GameCenterLeaderboardsLinkagesOfGameCenterGroupEndpoint:
        return GameCenterLeaderboardsLinkagesOfGameCenterGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboardsV2')
    def game_center_leaderboards_v2_linkage(self) -> GameCenterLeaderboardsV2LinkageOfGameCenterGroupEndpoint:
        return GameCenterLeaderboardsV2LinkageOfGameCenterGroupEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GameCenterGroupEndpoint:
        '''Fields to return for included related types.

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupEndpoint
        '''
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAILS = 'gameCenterDetails'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        GAME_CENTER_LEADERBOARDS_V2 = 'gameCenterLeaderboardsV2'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        GAME_CENTER_LEADERBOARD_SETS_V2 = 'gameCenterLeaderboardSetsV2'
        GAME_CENTER_ACHIEVEMENTS = 'gameCenterAchievements'
        GAME_CENTER_ACHIEVEMENTS_V2 = 'gameCenterAchievementsV2'
        GAME_CENTER_ACTIVITIES = 'gameCenterActivities'
        GAME_CENTER_CHALLENGES = 'gameCenterChallenges'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_achievements: int=None, game_center_achievements_v2: int=None, game_center_activities: int=None, game_center_challenges: int=None, game_center_details: int=None, game_center_leaderboard_sets: int=None, game_center_leaderboard_sets_v2: int=None, game_center_leaderboards: int=None, game_center_leaderboards_v2: int=None) -> GameCenterGroupEndpoint:
        '''Number of included related resources to return.

        :param game_center_achievements: maximum number of related gameCenterAchievements returned (when they are included). The maximum limit is 50
        :type game_center_achievements: int = None

        :param game_center_achievements_v2: maximum number of related gameCenterAchievementsV2 returned (when they are included). The maximum limit is 50
        :type game_center_achievements_v2: int = None

        :param game_center_activities: maximum number of related gameCenterActivities returned (when they are included). The maximum limit is 50
        :type game_center_activities: int = None

        :param game_center_challenges: maximum number of related gameCenterChallenges returned (when they are included). The maximum limit is 50
        :type game_center_challenges: int = None

        :param game_center_details: maximum number of related gameCenterDetails returned (when they are included). The maximum limit is 50
        :type game_center_details: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param game_center_leaderboard_sets_v2: maximum number of related gameCenterLeaderboardSetsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets_v2: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param game_center_leaderboards_v2: maximum number of related gameCenterLeaderboardsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards_v2: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupEndpoint
        '''
        if game_center_achievements and game_center_achievements > 50:
            raise ValueError(f'The maximum limit of game_center_achievements is 50')
        if game_center_achievements: self._set_limit(game_center_achievements, 'gameCenterAchievements')

        if game_center_achievements_v2 and game_center_achievements_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_achievements_v2 is 50')
        if game_center_achievements_v2: self._set_limit(game_center_achievements_v2, 'gameCenterAchievementsV2')

        if game_center_activities and game_center_activities > 50:
            raise ValueError(f'The maximum limit of game_center_activities is 50')
        if game_center_activities: self._set_limit(game_center_activities, 'gameCenterActivities')

        if game_center_challenges and game_center_challenges > 50:
            raise ValueError(f'The maximum limit of game_center_challenges is 50')
        if game_center_challenges: self._set_limit(game_center_challenges, 'gameCenterChallenges')

        if game_center_details and game_center_details > 50:
            raise ValueError(f'The maximum limit of game_center_details is 50')
        if game_center_details: self._set_limit(game_center_details, 'gameCenterDetails')

        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if game_center_leaderboard_sets_v2 and game_center_leaderboard_sets_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets_v2 is 50')
        if game_center_leaderboard_sets_v2: self._set_limit(game_center_leaderboard_sets_v2, 'gameCenterLeaderboardSetsV2')

        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if game_center_leaderboards_v2 and game_center_leaderboards_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards_v2 is 50')
        if game_center_leaderboards_v2: self._set_limit(game_center_leaderboards_v2, 'gameCenterLeaderboardsV2')

        return self

    def get(self) -> GameCenterGroupResponse:
        '''Get the resource.

        :returns: Single GameCenterGroup
        :rtype: GameCenterGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupResponse.parse_obj(json)

    def update(self, request: GameCenterGroupUpdateRequest) -> GameCenterGroupResponse:
        '''Modify the resource.

        :param request: GameCenterGroup representation
        :type request: GameCenterGroupUpdateRequest

        :returns: Single GameCenterGroup
        :rtype: GameCenterGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterGroupResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterAchievementsLinkagesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterAchievements'

    def limit(self, number: int=None) -> GameCenterAchievementsLinkagesOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsLinkagesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterGroupGameCenterAchievementsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterAchievementsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterAchievementsLinkagesResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterGroupGameCenterAchievementsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterGroupGameCenterAchievementsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterAchievementsOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterAchievements'

    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None) -> GameCenterAchievementsOfGameCenterGroupEndpoint:
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
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterGroupEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterAchievementsOfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterGroupEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementsOfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None, releases: int=None) -> GameCenterAchievementsOfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterGroupEndpoint
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

    @deprecated
    def get(self) -> GameCenterAchievementsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterAchievements
        :rtype: GameCenterAchievementsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementsResponse.parse_obj(json)

class GameCenterAchievementsV2LinkageOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterAchievementsV2'

    def limit(self, number: int=None) -> GameCenterAchievementsV2LinkageOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2LinkageOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterGroupGameCenterAchievementsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterAchievementsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterAchievementsV2LinkagesResponse.parse_obj(json)

    def update(self, request: GameCenterGroupGameCenterAchievementsV2LinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterGroupGameCenterAchievementsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterAchievementsV2OfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterAchievementsV2'

    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]]=None) -> GameCenterAchievementsV2OfGameCenterGroupEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_achievement_version: the fields to include for returned resources of type gameCenterAchievementVersions
        :type game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterGroupEndpoint
        '''
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_achievement_version: self._set_fields('gameCenterAchievementVersions',game_center_achievement_version if type(game_center_achievement_version) is list else [game_center_achievement_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        ACTIVITY = 'activity'
        VERSIONS = 'versions'

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterAchievementsV2OfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterGroupEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementsV2OfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, versions: int=None) -> GameCenterAchievementsV2OfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterAchievementsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterAchievements
        :rtype: GameCenterAchievementsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementsV2Response.parse_obj(json)

class GameCenterActivitiesLinkagesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterActivities'

    def limit(self, number: int=None) -> GameCenterActivitiesLinkagesOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivitiesLinkagesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterGroupGameCenterActivitiesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterActivitiesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterActivitiesLinkagesResponse.parse_obj(json)

class GameCenterActivitiesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterActivities'

    def fields(self, *, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None) -> GameCenterActivitiesOfGameCenterGroupEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_activity_version: the fields to include for returned resources of type gameCenterActivityVersions
        :type game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivitiesOfGameCenterGroupEndpoint
        '''
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
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

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterActivitiesOfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivitiesOfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, achievements: int=None, achievements_v2: int=None, leaderboards: int=None, leaderboards_v2: int=None, versions: int=None) -> GameCenterActivitiesOfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

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
        :rtype: applaud.endpoints.GameCenterActivitiesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
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

    def get(self) -> GameCenterActivitiesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterActivities
        :rtype: GameCenterActivitiesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivitiesResponse.parse_obj(json)

class GameCenterChallengesLinkagesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterChallenges'

    def limit(self, number: int=None) -> GameCenterChallengesLinkagesOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesLinkagesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterGroupGameCenterChallengesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterChallengesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterChallengesLinkagesResponse.parse_obj(json)

class GameCenterChallengesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterChallenges'

    def fields(self, *, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None) -> GameCenterChallengesOfGameCenterGroupEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_challenge_version: the fields to include for returned resources of type gameCenterChallengeVersions
        :type game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterGroupEndpoint
        '''
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_challenge_version: self._set_fields('gameCenterChallengeVersions',game_center_challenge_version if type(game_center_challenge_version) is list else [game_center_challenge_version])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        VERSIONS = 'versions'
        LEADERBOARD = 'leaderboard'
        LEADERBOARD_V2 = 'leaderboardV2'

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterChallengesOfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterGroupEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterChallengesOfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, versions: int=None) -> GameCenterChallengesOfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterChallengesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterChallenges
        :rtype: GameCenterChallengesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengesResponse.parse_obj(json)

class GameCenterDetailsLinkagesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterDetails'

    def limit(self, number: int=None) -> GameCenterDetailsLinkagesOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailsLinkagesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterGroupGameCenterDetailsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterDetailsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterDetailsLinkagesResponse.parse_obj(json)

class GameCenterDetailsOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterDetails'

    def fields(self, *, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, app: Union[AppField, list[AppField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]]=None, game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> GameCenterDetailsOfGameCenterGroupEndpoint:
        '''Fields to return for included related types.

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param game_center_app_version: the fields to include for returned resources of type gameCenterAppVersions
        :type game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :param game_center_achievement_release: the fields to include for returned resources of type gameCenterAchievementReleases
        :type game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]] = None

        :param game_center_activity_version_release: the fields to include for returned resources of type gameCenterActivityVersionReleases
        :type game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]] = None

        :param game_center_challenge_version_release: the fields to include for returned resources of type gameCenterChallengeVersionReleases
        :type game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]] = None

        :param game_center_leaderboard_release: the fields to include for returned resources of type gameCenterLeaderboardReleases
        :type game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]] = None

        :param game_center_leaderboard_set_release: the fields to include for returned resources of type gameCenterLeaderboardSetReleases
        :type game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailsOfGameCenterGroupEndpoint
        '''
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if game_center_app_version: self._set_fields('gameCenterAppVersions',game_center_app_version if type(game_center_app_version) is list else [game_center_app_version])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        if game_center_achievement_release: self._set_fields('gameCenterAchievementReleases',game_center_achievement_release if type(game_center_achievement_release) is list else [game_center_achievement_release])
        if game_center_activity_version_release: self._set_fields('gameCenterActivityVersionReleases',game_center_activity_version_release if type(game_center_activity_version_release) is list else [game_center_activity_version_release])
        if game_center_challenge_version_release: self._set_fields('gameCenterChallengeVersionReleases',game_center_challenge_version_release if type(game_center_challenge_version_release) is list else [game_center_challenge_version_release])
        if game_center_leaderboard_release: self._set_fields('gameCenterLeaderboardReleases',game_center_leaderboard_release if type(game_center_leaderboard_release) is list else [game_center_leaderboard_release])
        if game_center_leaderboard_set_release: self._set_fields('gameCenterLeaderboardSetReleases',game_center_leaderboard_set_release if type(game_center_leaderboard_set_release) is list else [game_center_leaderboard_set_release])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        GAME_CENTER_APP_VERSIONS = 'gameCenterAppVersions'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        GAME_CENTER_LEADERBOARDS_V2 = 'gameCenterLeaderboardsV2'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        GAME_CENTER_LEADERBOARD_SETS_V2 = 'gameCenterLeaderboardSetsV2'
        GAME_CENTER_ACHIEVEMENTS = 'gameCenterAchievements'
        GAME_CENTER_ACHIEVEMENTS_V2 = 'gameCenterAchievementsV2'
        GAME_CENTER_ACTIVITIES = 'gameCenterActivities'
        GAME_CENTER_CHALLENGES = 'gameCenterChallenges'
        DEFAULT_LEADERBOARD = 'defaultLeaderboard'
        DEFAULT_LEADERBOARD_V2 = 'defaultLeaderboardV2'
        DEFAULT_GROUP_LEADERBOARD = 'defaultGroupLeaderboard'
        DEFAULT_GROUP_LEADERBOARD_V2 = 'defaultGroupLeaderboardV2'
        ACHIEVEMENT_RELEASES = 'achievementReleases'
        ACTIVITY_RELEASES = 'activityReleases'
        CHALLENGE_RELEASES = 'challengeReleases'
        LEADERBOARD_RELEASES = 'leaderboardReleases'
        LEADERBOARD_SET_RELEASES = 'leaderboardSetReleases'
        CHALLENGES_MINIMUM_PLATFORM_VERSIONS = 'challengesMinimumPlatformVersions'

    def filter(self, *, game_center_app_versions_enabled: Union[str, list[str]]=None) -> GameCenterDetailsOfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param game_center_app_versions_enabled: filter by attribute 'gameCenterAppVersions.enabled'
        :type game_center_app_versions_enabled: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailsOfGameCenterGroupEndpoint
        '''
        if game_center_app_versions_enabled: self._set_filter('gameCenterAppVersions.enabled', game_center_app_versions_enabled if type(game_center_app_versions_enabled) is list else [game_center_app_versions_enabled])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterDetailsOfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailsOfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_app_versions: int=None, game_center_leaderboards: int=None, game_center_leaderboards_v2: int=None, game_center_leaderboard_sets: int=None, game_center_leaderboard_sets_v2: int=None, game_center_achievements: int=None, game_center_achievements_v2: int=None, game_center_activities: int=None, game_center_challenges: int=None, achievement_releases: int=None, activity_releases: int=None, challenge_releases: int=None, leaderboard_releases: int=None, leaderboard_set_releases: int=None, challenges_minimum_platform_versions: int=None) -> GameCenterDetailsOfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_app_versions: maximum number of related gameCenterAppVersions returned (when they are included). The maximum limit is 50
        :type game_center_app_versions: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param game_center_leaderboards_v2: maximum number of related gameCenterLeaderboardsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards_v2: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param game_center_leaderboard_sets_v2: maximum number of related gameCenterLeaderboardSetsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets_v2: int = None

        :param game_center_achievements: maximum number of related gameCenterAchievements returned (when they are included). The maximum limit is 50
        :type game_center_achievements: int = None

        :param game_center_achievements_v2: maximum number of related gameCenterAchievementsV2 returned (when they are included). The maximum limit is 50
        :type game_center_achievements_v2: int = None

        :param game_center_activities: maximum number of related gameCenterActivities returned (when they are included). The maximum limit is 50
        :type game_center_activities: int = None

        :param game_center_challenges: maximum number of related gameCenterChallenges returned (when they are included). The maximum limit is 50
        :type game_center_challenges: int = None

        :param achievement_releases: maximum number of related achievementReleases returned (when they are included). The maximum limit is 50
        :type achievement_releases: int = None

        :param activity_releases: maximum number of related activityReleases returned (when they are included). The maximum limit is 50
        :type activity_releases: int = None

        :param challenge_releases: maximum number of related challengeReleases returned (when they are included). The maximum limit is 50
        :type challenge_releases: int = None

        :param leaderboard_releases: maximum number of related leaderboardReleases returned (when they are included). The maximum limit is 50
        :type leaderboard_releases: int = None

        :param leaderboard_set_releases: maximum number of related leaderboardSetReleases returned (when they are included). The maximum limit is 50
        :type leaderboard_set_releases: int = None

        :param challenges_minimum_platform_versions: maximum number of related challengesMinimumPlatformVersions returned (when they are included). The maximum limit is 50
        :type challenges_minimum_platform_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailsOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if game_center_app_versions and game_center_app_versions > 50:
            raise ValueError(f'The maximum limit of game_center_app_versions is 50')
        if game_center_app_versions: self._set_limit(game_center_app_versions, 'gameCenterAppVersions')

        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if game_center_leaderboards_v2 and game_center_leaderboards_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards_v2 is 50')
        if game_center_leaderboards_v2: self._set_limit(game_center_leaderboards_v2, 'gameCenterLeaderboardsV2')

        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if game_center_leaderboard_sets_v2 and game_center_leaderboard_sets_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets_v2 is 50')
        if game_center_leaderboard_sets_v2: self._set_limit(game_center_leaderboard_sets_v2, 'gameCenterLeaderboardSetsV2')

        if game_center_achievements and game_center_achievements > 50:
            raise ValueError(f'The maximum limit of game_center_achievements is 50')
        if game_center_achievements: self._set_limit(game_center_achievements, 'gameCenterAchievements')

        if game_center_achievements_v2 and game_center_achievements_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_achievements_v2 is 50')
        if game_center_achievements_v2: self._set_limit(game_center_achievements_v2, 'gameCenterAchievementsV2')

        if game_center_activities and game_center_activities > 50:
            raise ValueError(f'The maximum limit of game_center_activities is 50')
        if game_center_activities: self._set_limit(game_center_activities, 'gameCenterActivities')

        if game_center_challenges and game_center_challenges > 50:
            raise ValueError(f'The maximum limit of game_center_challenges is 50')
        if game_center_challenges: self._set_limit(game_center_challenges, 'gameCenterChallenges')

        if achievement_releases and achievement_releases > 50:
            raise ValueError(f'The maximum limit of achievement_releases is 50')
        if achievement_releases: self._set_limit(achievement_releases, 'achievementReleases')

        if activity_releases and activity_releases > 50:
            raise ValueError(f'The maximum limit of activity_releases is 50')
        if activity_releases: self._set_limit(activity_releases, 'activityReleases')

        if challenge_releases and challenge_releases > 50:
            raise ValueError(f'The maximum limit of challenge_releases is 50')
        if challenge_releases: self._set_limit(challenge_releases, 'challengeReleases')

        if leaderboard_releases and leaderboard_releases > 50:
            raise ValueError(f'The maximum limit of leaderboard_releases is 50')
        if leaderboard_releases: self._set_limit(leaderboard_releases, 'leaderboardReleases')

        if leaderboard_set_releases and leaderboard_set_releases > 50:
            raise ValueError(f'The maximum limit of leaderboard_set_releases is 50')
        if leaderboard_set_releases: self._set_limit(leaderboard_set_releases, 'leaderboardSetReleases')

        if challenges_minimum_platform_versions and challenges_minimum_platform_versions > 50:
            raise ValueError(f'The maximum limit of challenges_minimum_platform_versions is 50')
        if challenges_minimum_platform_versions: self._set_limit(challenges_minimum_platform_versions, 'challengesMinimumPlatformVersions')

        return self

    def get(self) -> GameCenterDetailsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterDetails
        :rtype: GameCenterDetailsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailsResponse.parse_obj(json)

class GameCenterLeaderboardSetsLinkagesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboardSets'

    def limit(self, number: int=None) -> GameCenterLeaderboardSetsLinkagesOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsLinkagesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterGroupGameCenterLeaderboardSetsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterLeaderboardSetsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterLeaderboardSetsLinkagesResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterGroupGameCenterLeaderboardSetsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterGroupGameCenterLeaderboardSetsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardSetsOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterLeaderboardSets'

    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None) -> GameCenterLeaderboardSetsOfGameCenterGroupEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterGroupEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardSetsOfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterGroupEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetsOfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None, game_center_leaderboards: int=None, releases: int=None) -> GameCenterLeaderboardSetsOfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
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
    def get(self) -> GameCenterLeaderboardSetsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardSets
        :rtype: GameCenterLeaderboardSetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetsResponse.parse_obj(json)

class GameCenterLeaderboardSetsV2LinkageOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboardSetsV2'

    def limit(self, number: int=None) -> GameCenterLeaderboardSetsV2LinkageOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2LinkageOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterGroupGameCenterLeaderboardSetsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterLeaderboardSetsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterLeaderboardSetsV2LinkagesResponse.parse_obj(json)

    def update(self, request: GameCenterGroupGameCenterLeaderboardSetsV2LinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterGroupGameCenterLeaderboardSetsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterLeaderboardSetsV2'

    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]]=None) -> GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set_version: the fields to include for returned resources of type gameCenterLeaderboardSetVersions
        :type game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint
        '''
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set_version: self._set_fields('gameCenterLeaderboardSetVersions',game_center_leaderboard_set_version if type(game_center_leaderboard_set_version) is list else [game_center_leaderboard_set_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        VERSIONS = 'versions'

    def filter(self, *, reference_name: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboards: int=None, versions: int=None) -> GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterLeaderboardSetsV2Response:
        '''Get one or more resources.

        :returns: List of GameCenterLeaderboardSets
        :rtype: GameCenterLeaderboardSetsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetsV2Response.parse_obj(json)

class GameCenterLeaderboardsLinkagesOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboards'

    def limit(self, number: int=None) -> GameCenterLeaderboardsLinkagesOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsLinkagesOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterGroupGameCenterLeaderboardsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterLeaderboardsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterLeaderboardsLinkagesResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterGroupGameCenterLeaderboardsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterGroupGameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardsOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterLeaderboards'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GameCenterLeaderboardsOfGameCenterGroupEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterGroupEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardsOfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterGroupEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardsOfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboard_sets: int=None, localizations: int=None, releases: int=None) -> GameCenterLeaderboardsOfGameCenterGroupEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterGroupEndpoint
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

class GameCenterLeaderboardsV2LinkageOfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/relationships/gameCenterLeaderboardsV2'

    def limit(self, number: int=None) -> GameCenterLeaderboardsV2LinkageOfGameCenterGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2LinkageOfGameCenterGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterGroupGameCenterLeaderboardsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterGroupGameCenterLeaderboardsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterGroupGameCenterLeaderboardsV2LinkagesResponse.parse_obj(json)

    def update(self, request: GameCenterGroupGameCenterLeaderboardsV2LinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterGroupGameCenterLeaderboardsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardsV2OfGameCenterGroupEndpoint(IDEndpoint):
    path = '/v1/gameCenterGroups/{id}/gameCenterLeaderboardsV2'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None) -> GameCenterLeaderboardsV2OfGameCenterGroupEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterGroupEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardsV2OfGameCenterGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterGroupEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardsV2OfGameCenterGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboard_sets: int=None, versions: int=None) -> GameCenterLeaderboardsV2OfGameCenterGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterGroupEndpoint
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

