from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterDetailsEndpoint(Endpoint):
    path = '/v1/gameCenterDetails'

    def create(self, request: GameCenterDetailCreateRequest) -> GameCenterDetailResponse:
        '''Create the resource.

        :param request: GameCenterDetail representation
        :type request: GameCenterDetailCreateRequest

        :returns: Single GameCenterDetail
        :rtype: GameCenterDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterDetailResponse.parse_obj(json)

class GameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}'

    @endpoint('/v1/gameCenterDetails/{id}/achievementReleases')
    def achievement_releases(self) -> AchievementReleasesOfGameCenterDetailEndpoint:
        return AchievementReleasesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/activityReleases')
    def activity_releases(self) -> ActivityReleasesOfGameCenterDetailEndpoint:
        return ActivityReleasesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/challengeReleases')
    def challenge_releases(self) -> ChallengeReleasesOfGameCenterDetailEndpoint:
        return ChallengeReleasesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterAchievements')
    def game_center_achievements(self) -> GameCenterAchievementsOfGameCenterDetailEndpoint:
        return GameCenterAchievementsOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterAchievementsV2')
    def game_center_achievements_v2(self) -> GameCenterAchievementsV2OfGameCenterDetailEndpoint:
        return GameCenterAchievementsV2OfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterActivities')
    def game_center_activities(self) -> GameCenterActivitiesOfGameCenterDetailEndpoint:
        return GameCenterActivitiesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterAppVersions')
    def game_center_app_versions(self) -> GameCenterAppVersionsOfGameCenterDetailEndpoint:
        return GameCenterAppVersionsOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterChallenges')
    def game_center_challenges(self) -> GameCenterChallengesOfGameCenterDetailEndpoint:
        return GameCenterChallengesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterGroup')
    def game_center_group(self) -> GameCenterGroupOfGameCenterDetailEndpoint:
        return GameCenterGroupOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterLeaderboardSets')
    def game_center_leaderboard_sets(self) -> GameCenterLeaderboardSetsOfGameCenterDetailEndpoint:
        return GameCenterLeaderboardSetsOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterLeaderboardSetsV2')
    def game_center_leaderboard_sets_v2(self) -> GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint:
        return GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterLeaderboards')
    def game_center_leaderboards(self) -> GameCenterLeaderboardsOfGameCenterDetailEndpoint:
        return GameCenterLeaderboardsOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/gameCenterLeaderboardsV2')
    def game_center_leaderboards_v2(self) -> GameCenterLeaderboardsV2OfGameCenterDetailEndpoint:
        return GameCenterLeaderboardsV2OfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/leaderboardReleases')
    def leaderboard_releases(self) -> LeaderboardReleasesOfGameCenterDetailEndpoint:
        return LeaderboardReleasesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/leaderboardSetReleases')
    def leaderboard_set_releases(self) -> LeaderboardSetReleasesOfGameCenterDetailEndpoint:
        return LeaderboardSetReleasesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/metrics/classicMatchmakingRequests')
    def classic_matchmaking_requests(self) -> ClassicMatchmakingRequestsOfGameCenterDetailEndpoint:
        return ClassicMatchmakingRequestsOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/metrics/ruleBasedMatchmakingRequests')
    def rule_based_matchmaking_requests(self) -> RuleBasedMatchmakingRequestsOfGameCenterDetailEndpoint:
        return RuleBasedMatchmakingRequestsOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/achievementReleases')
    def achievement_releases_linkages(self) -> AchievementReleasesLinkagesOfGameCenterDetailEndpoint:
        return AchievementReleasesLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/activityReleases')
    def activity_releases_linkages(self) -> ActivityReleasesLinkagesOfGameCenterDetailEndpoint:
        return ActivityReleasesLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/challengeReleases')
    def challenge_releases_linkages(self) -> ChallengeReleasesLinkagesOfGameCenterDetailEndpoint:
        return ChallengeReleasesLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/challengesMinimumPlatformVersions')
    def challenges_minimum_platform_versions_linkages(self) -> ChallengesMinimumPlatformVersionsLinkagesOfGameCenterDetailEndpoint:
        return ChallengesMinimumPlatformVersionsLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterAchievements')
    def game_center_achievements_linkages(self) -> GameCenterAchievementsLinkagesOfGameCenterDetailEndpoint:
        return GameCenterAchievementsLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterAchievementsV2')
    def game_center_achievements_v2_linkage(self) -> GameCenterAchievementsV2LinkageOfGameCenterDetailEndpoint:
        return GameCenterAchievementsV2LinkageOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterActivities')
    def game_center_activities_linkages(self) -> GameCenterActivitiesLinkagesOfGameCenterDetailEndpoint:
        return GameCenterActivitiesLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterAppVersions')
    def game_center_app_versions_linkages(self) -> GameCenterAppVersionsLinkagesOfGameCenterDetailEndpoint:
        return GameCenterAppVersionsLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterChallenges')
    def game_center_challenges_linkages(self) -> GameCenterChallengesLinkagesOfGameCenterDetailEndpoint:
        return GameCenterChallengesLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterGroup')
    def game_center_group_linkage(self) -> GameCenterGroupLinkageOfGameCenterDetailEndpoint:
        return GameCenterGroupLinkageOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardSets')
    def game_center_leaderboard_sets_linkages(self) -> GameCenterLeaderboardSetsLinkagesOfGameCenterDetailEndpoint:
        return GameCenterLeaderboardSetsLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardSetsV2')
    def game_center_leaderboard_sets_v2_linkage(self) -> GameCenterLeaderboardSetsV2LinkageOfGameCenterDetailEndpoint:
        return GameCenterLeaderboardSetsV2LinkageOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboards')
    def game_center_leaderboards_linkages(self) -> GameCenterLeaderboardsLinkagesOfGameCenterDetailEndpoint:
        return GameCenterLeaderboardsLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardsV2')
    def game_center_leaderboards_v2_linkage(self) -> GameCenterLeaderboardsV2LinkageOfGameCenterDetailEndpoint:
        return GameCenterLeaderboardsV2LinkageOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/leaderboardReleases')
    def leaderboard_releases_linkages(self) -> LeaderboardReleasesLinkagesOfGameCenterDetailEndpoint:
        return LeaderboardReleasesLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterDetails/{id}/relationships/leaderboardSetReleases')
    def leaderboard_set_releases_linkages(self) -> LeaderboardSetReleasesLinkagesOfGameCenterDetailEndpoint:
        return LeaderboardSetReleasesLinkagesOfGameCenterDetailEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]]=None, game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None) -> GameCenterDetailEndpoint:
        '''Fields to return for included related types.

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

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

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailEndpoint
        '''
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
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

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, achievement_releases: int=None, activity_releases: int=None, challenge_releases: int=None, challenges_minimum_platform_versions: int=None, game_center_achievements: int=None, game_center_achievements_v2: int=None, game_center_activities: int=None, game_center_app_versions: int=None, game_center_challenges: int=None, game_center_leaderboard_sets: int=None, game_center_leaderboard_sets_v2: int=None, game_center_leaderboards: int=None, game_center_leaderboards_v2: int=None, leaderboard_releases: int=None, leaderboard_set_releases: int=None) -> GameCenterDetailEndpoint:
        '''Number of included related resources to return.

        :param achievement_releases: maximum number of related achievementReleases returned (when they are included). The maximum limit is 50
        :type achievement_releases: int = None

        :param activity_releases: maximum number of related activityReleases returned (when they are included). The maximum limit is 50
        :type activity_releases: int = None

        :param challenge_releases: maximum number of related challengeReleases returned (when they are included). The maximum limit is 50
        :type challenge_releases: int = None

        :param challenges_minimum_platform_versions: maximum number of related challengesMinimumPlatformVersions returned (when they are included). The maximum limit is 50
        :type challenges_minimum_platform_versions: int = None

        :param game_center_achievements: maximum number of related gameCenterAchievements returned (when they are included). The maximum limit is 50
        :type game_center_achievements: int = None

        :param game_center_achievements_v2: maximum number of related gameCenterAchievementsV2 returned (when they are included). The maximum limit is 50
        :type game_center_achievements_v2: int = None

        :param game_center_activities: maximum number of related gameCenterActivities returned (when they are included). The maximum limit is 50
        :type game_center_activities: int = None

        :param game_center_app_versions: maximum number of related gameCenterAppVersions returned (when they are included). The maximum limit is 50
        :type game_center_app_versions: int = None

        :param game_center_challenges: maximum number of related gameCenterChallenges returned (when they are included). The maximum limit is 50
        :type game_center_challenges: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param game_center_leaderboard_sets_v2: maximum number of related gameCenterLeaderboardSetsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets_v2: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param game_center_leaderboards_v2: maximum number of related gameCenterLeaderboardsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards_v2: int = None

        :param leaderboard_releases: maximum number of related leaderboardReleases returned (when they are included). The maximum limit is 50
        :type leaderboard_releases: int = None

        :param leaderboard_set_releases: maximum number of related leaderboardSetReleases returned (when they are included). The maximum limit is 50
        :type leaderboard_set_releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailEndpoint
        '''
        if achievement_releases and achievement_releases > 50:
            raise ValueError(f'The maximum limit of achievement_releases is 50')
        if achievement_releases: self._set_limit(achievement_releases, 'achievementReleases')

        if activity_releases and activity_releases > 50:
            raise ValueError(f'The maximum limit of activity_releases is 50')
        if activity_releases: self._set_limit(activity_releases, 'activityReleases')

        if challenge_releases and challenge_releases > 50:
            raise ValueError(f'The maximum limit of challenge_releases is 50')
        if challenge_releases: self._set_limit(challenge_releases, 'challengeReleases')

        if challenges_minimum_platform_versions and challenges_minimum_platform_versions > 50:
            raise ValueError(f'The maximum limit of challenges_minimum_platform_versions is 50')
        if challenges_minimum_platform_versions: self._set_limit(challenges_minimum_platform_versions, 'challengesMinimumPlatformVersions')

        if game_center_achievements and game_center_achievements > 50:
            raise ValueError(f'The maximum limit of game_center_achievements is 50')
        if game_center_achievements: self._set_limit(game_center_achievements, 'gameCenterAchievements')

        if game_center_achievements_v2 and game_center_achievements_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_achievements_v2 is 50')
        if game_center_achievements_v2: self._set_limit(game_center_achievements_v2, 'gameCenterAchievementsV2')

        if game_center_activities and game_center_activities > 50:
            raise ValueError(f'The maximum limit of game_center_activities is 50')
        if game_center_activities: self._set_limit(game_center_activities, 'gameCenterActivities')

        if game_center_app_versions and game_center_app_versions > 50:
            raise ValueError(f'The maximum limit of game_center_app_versions is 50')
        if game_center_app_versions: self._set_limit(game_center_app_versions, 'gameCenterAppVersions')

        if game_center_challenges and game_center_challenges > 50:
            raise ValueError(f'The maximum limit of game_center_challenges is 50')
        if game_center_challenges: self._set_limit(game_center_challenges, 'gameCenterChallenges')

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

        if leaderboard_releases and leaderboard_releases > 50:
            raise ValueError(f'The maximum limit of leaderboard_releases is 50')
        if leaderboard_releases: self._set_limit(leaderboard_releases, 'leaderboardReleases')

        if leaderboard_set_releases and leaderboard_set_releases > 50:
            raise ValueError(f'The maximum limit of leaderboard_set_releases is 50')
        if leaderboard_set_releases: self._set_limit(leaderboard_set_releases, 'leaderboardSetReleases')

        return self

    def get(self) -> GameCenterDetailResponse:
        '''Get the resource.

        :returns: Single GameCenterDetail
        :rtype: GameCenterDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailResponse.parse_obj(json)

    def update(self, request: GameCenterDetailUpdateRequest) -> GameCenterDetailResponse:
        '''Modify the resource.

        :param request: GameCenterDetail representation
        :type request: GameCenterDetailUpdateRequest

        :returns: Single GameCenterDetail
        :rtype: GameCenterDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterDetailResponse.parse_obj(json)

class AchievementReleasesLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/achievementReleases'

    def limit(self, number: int=None) -> AchievementReleasesLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AchievementReleasesLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailAchievementReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailAchievementReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailAchievementReleasesLinkagesResponse.parse_obj(json)

class AchievementReleasesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/achievementReleases'

    def fields(self, *, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None) -> AchievementReleasesOfGameCenterDetailEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_release: the fields to include for returned resources of type gameCenterAchievementReleases
        :type game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :returns: self
        :rtype: applaud.endpoints.AchievementReleasesOfGameCenterDetailEndpoint
        '''
        if game_center_achievement_release: self._set_fields('gameCenterAchievementReleases',game_center_achievement_release if type(game_center_achievement_release) is list else [game_center_achievement_release])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_ACHIEVEMENT = 'gameCenterAchievement'

    def filter(self, *, live: Union[str, list[str]]=None, game_center_achievement: Union[str, list[str]]=None) -> AchievementReleasesOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param live: filter by attribute 'live'
        :type live: Union[str, list[str]] = None

        :param game_center_achievement: filter by id(s) of related 'gameCenterAchievement'
        :type game_center_achievement: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AchievementReleasesOfGameCenterDetailEndpoint
        '''
        if live: self._set_filter('live', live if type(live) is list else [live])
        
        if game_center_achievement: self._set_filter('gameCenterAchievement', game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AchievementReleasesOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AchievementReleasesOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AchievementReleasesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AchievementReleasesOfGameCenterDetailEndpoint
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

class ActivityReleasesLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/activityReleases'

    def limit(self, number: int=None) -> ActivityReleasesLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ActivityReleasesLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailActivityReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailActivityReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailActivityReleasesLinkagesResponse.parse_obj(json)

class ActivityReleasesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/activityReleases'

    def fields(self, *, game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]]=None, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None) -> ActivityReleasesOfGameCenterDetailEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_version_release: the fields to include for returned resources of type gameCenterActivityVersionReleases
        :type game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]] = None

        :param game_center_activity_version: the fields to include for returned resources of type gameCenterActivityVersions
        :type game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.ActivityReleasesOfGameCenterDetailEndpoint
        '''
        if game_center_activity_version_release: self._set_fields('gameCenterActivityVersionReleases',game_center_activity_version_release if type(game_center_activity_version_release) is list else [game_center_activity_version_release])
        if game_center_activity_version: self._set_fields('gameCenterActivityVersions',game_center_activity_version if type(game_center_activity_version) is list else [game_center_activity_version])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'

    def include(self, relationship: Union[Include, list[Include]]) -> ActivityReleasesOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ActivityReleasesOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ActivityReleasesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ActivityReleasesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterActivityVersionReleasesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterActivityVersionReleases
        :rtype: GameCenterActivityVersionReleasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityVersionReleasesResponse.parse_obj(json)

class ChallengeReleasesLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/challengeReleases'

    def limit(self, number: int=None) -> ChallengeReleasesLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ChallengeReleasesLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailChallengeReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailChallengeReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailChallengeReleasesLinkagesResponse.parse_obj(json)

class ChallengeReleasesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/challengeReleases'

    def fields(self, *, game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]]=None, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None) -> ChallengeReleasesOfGameCenterDetailEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_version_release: the fields to include for returned resources of type gameCenterChallengeVersionReleases
        :type game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]] = None

        :param game_center_challenge_version: the fields to include for returned resources of type gameCenterChallengeVersions
        :type game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.ChallengeReleasesOfGameCenterDetailEndpoint
        '''
        if game_center_challenge_version_release: self._set_fields('gameCenterChallengeVersionReleases',game_center_challenge_version_release if type(game_center_challenge_version_release) is list else [game_center_challenge_version_release])
        if game_center_challenge_version: self._set_fields('gameCenterChallengeVersions',game_center_challenge_version if type(game_center_challenge_version) is list else [game_center_challenge_version])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'

    def include(self, relationship: Union[Include, list[Include]]) -> ChallengeReleasesOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ChallengeReleasesOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ChallengeReleasesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ChallengeReleasesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterChallengeVersionReleasesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterChallengeVersionReleases
        :rtype: GameCenterChallengeVersionReleasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeVersionReleasesResponse.parse_obj(json)

class ChallengesMinimumPlatformVersionsLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/challengesMinimumPlatformVersions'

    def update(self, request: GameCenterDetailChallengesMinimumPlatformVersionsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterDetailChallengesMinimumPlatformVersionsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterAchievementsLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterAchievements'

    def limit(self, number: int=None) -> GameCenterAchievementsLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailGameCenterAchievementsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterAchievementsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterAchievementsLinkagesResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterDetailGameCenterAchievementsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterDetailGameCenterAchievementsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterAchievementsOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterAchievements'

    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_achievement_localization: Union[GameCenterAchievementLocalizationField, list[GameCenterAchievementLocalizationField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None) -> GameCenterAchievementsOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterDetailEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterAchievementsOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterDetailEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementsOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None, releases: int=None) -> GameCenterAchievementsOfGameCenterDetailEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsOfGameCenterDetailEndpoint
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

class GameCenterAchievementsV2LinkageOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterAchievementsV2'

    def limit(self, number: int=None) -> GameCenterAchievementsV2LinkageOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2LinkageOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterDetailGameCenterAchievementsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterAchievementsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterAchievementsV2LinkagesResponse.parse_obj(json)

    def update(self, request: GameCenterDetailGameCenterAchievementsV2LinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterDetailGameCenterAchievementsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterAchievementsV2OfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterAchievementsV2'

    def fields(self, *, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]]=None) -> GameCenterAchievementsV2OfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterDetailEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterAchievementsV2OfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterDetailEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementsV2OfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, versions: int=None) -> GameCenterAchievementsV2OfGameCenterDetailEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementsV2OfGameCenterDetailEndpoint
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

class GameCenterActivitiesLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterActivities'

    def limit(self, number: int=None) -> GameCenterActivitiesLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivitiesLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterDetailGameCenterActivitiesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterActivitiesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterActivitiesLinkagesResponse.parse_obj(json)

class GameCenterActivitiesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterActivities'

    def fields(self, *, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None) -> GameCenterActivitiesOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterActivitiesOfGameCenterDetailEndpoint
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

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterActivitiesOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivitiesOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, achievements: int=None, achievements_v2: int=None, leaderboards: int=None, leaderboards_v2: int=None, versions: int=None) -> GameCenterActivitiesOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterActivitiesOfGameCenterDetailEndpoint
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

class GameCenterAppVersionsLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterAppVersions'

    def limit(self, number: int=None) -> GameCenterAppVersionsLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionsLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterDetailGameCenterAppVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterAppVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterAppVersionsLinkagesResponse.parse_obj(json)

class GameCenterAppVersionsOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterAppVersions'

    def fields(self, *, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> GameCenterAppVersionsOfGameCenterDetailEndpoint:
        '''Fields to return for included related types.

        :param game_center_app_version: the fields to include for returned resources of type gameCenterAppVersions
        :type game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionsOfGameCenterDetailEndpoint
        '''
        if game_center_app_version: self._set_fields('gameCenterAppVersions',game_center_app_version if type(game_center_app_version) is list else [game_center_app_version])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        COMPATIBILITY_VERSIONS = 'compatibilityVersions'
        APP_STORE_VERSION = 'appStoreVersion'

    def filter(self, *, enabled: Union[str, list[str]]=None) -> GameCenterAppVersionsOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param enabled: filter by attribute 'enabled'
        :type enabled: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionsOfGameCenterDetailEndpoint
        '''
        if enabled: self._set_filter('enabled', enabled if type(enabled) is list else [enabled])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAppVersionsOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionsOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, compatibility_versions: int=None) -> GameCenterAppVersionsOfGameCenterDetailEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param compatibility_versions: maximum number of related compatibilityVersions returned (when they are included). The maximum limit is 50
        :type compatibility_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionsOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if compatibility_versions and compatibility_versions > 50:
            raise ValueError(f'The maximum limit of compatibility_versions is 50')
        if compatibility_versions: self._set_limit(compatibility_versions, 'compatibilityVersions')

        return self

    def get(self) -> GameCenterAppVersionsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterAppVersions
        :rtype: GameCenterAppVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAppVersionsResponse.parse_obj(json)

class GameCenterChallengesLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterChallenges'

    def limit(self, number: int=None) -> GameCenterChallengesLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterDetailGameCenterChallengesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterChallengesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterChallengesLinkagesResponse.parse_obj(json)

class GameCenterChallengesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterChallenges'

    def fields(self, *, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None) -> GameCenterChallengesOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterDetailEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterChallengesOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterDetailEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterChallengesOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, versions: int=None) -> GameCenterChallengesOfGameCenterDetailEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengesOfGameCenterDetailEndpoint
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

class GameCenterGroupLinkageOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterGroup'

    def get(self) -> GameCenterDetailGameCenterGroupLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterDetailGameCenterGroupLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterGroupLinkageResponse.parse_obj(json)

class GameCenterGroupOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterGroup'

    def fields(self, *, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GameCenterGroupOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterGroupOfGameCenterDetailEndpoint
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

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterGroupOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_details: int=None, game_center_leaderboards: int=None, game_center_leaderboards_v2: int=None, game_center_leaderboard_sets: int=None, game_center_leaderboard_sets_v2: int=None, game_center_achievements: int=None, game_center_achievements_v2: int=None, game_center_activities: int=None, game_center_challenges: int=None) -> GameCenterGroupOfGameCenterDetailEndpoint:
        '''Number of included related resources to return.

        :param game_center_details: maximum number of related gameCenterDetails returned (when they are included). The maximum limit is 50
        :type game_center_details: int = None

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

        :returns: self
        :rtype: applaud.endpoints.GameCenterGroupOfGameCenterDetailEndpoint
        '''
        if game_center_details and game_center_details > 50:
            raise ValueError(f'The maximum limit of game_center_details is 50')
        if game_center_details: self._set_limit(game_center_details, 'gameCenterDetails')

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

class GameCenterLeaderboardSetsLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardSets'

    def limit(self, number: int=None) -> GameCenterLeaderboardSetsLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailGameCenterLeaderboardSetsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterLeaderboardSetsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterLeaderboardSetsLinkagesResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterDetailGameCenterLeaderboardSetsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterDetailGameCenterLeaderboardSetsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardSetsOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterLeaderboardSets'

    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set_localization: Union[GameCenterLeaderboardSetLocalizationField, list[GameCenterLeaderboardSetLocalizationField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None) -> GameCenterLeaderboardSetsOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterDetailEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardSetsOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterDetailEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetsOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None, game_center_leaderboards: int=None, releases: int=None) -> GameCenterLeaderboardSetsOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsOfGameCenterDetailEndpoint
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

class GameCenterLeaderboardSetsV2LinkageOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardSetsV2'

    def limit(self, number: int=None) -> GameCenterLeaderboardSetsV2LinkageOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2LinkageOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterDetailGameCenterLeaderboardSetsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterLeaderboardSetsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterLeaderboardSetsV2LinkagesResponse.parse_obj(json)

    def update(self, request: GameCenterDetailGameCenterLeaderboardSetsV2LinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterDetailGameCenterLeaderboardSetsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterLeaderboardSetsV2'

    def fields(self, *, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]]=None) -> GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboards: int=None, versions: int=None) -> GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetsV2OfGameCenterDetailEndpoint
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

class GameCenterLeaderboardsLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboards'

    def limit(self, number: int=None) -> GameCenterLeaderboardsLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailGameCenterLeaderboardsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterLeaderboardsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterLeaderboardsLinkagesResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterDetailGameCenterLeaderboardsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterDetailGameCenterLeaderboardsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardsOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterLeaderboards'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_leaderboard_localization: Union[GameCenterLeaderboardLocalizationField, list[GameCenterLeaderboardLocalizationField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None) -> GameCenterLeaderboardsOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterDetailEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardsOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterDetailEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardsOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboard_sets: int=None, localizations: int=None, releases: int=None) -> GameCenterLeaderboardsOfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardsOfGameCenterDetailEndpoint
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

class GameCenterLeaderboardsV2LinkageOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardsV2'

    def limit(self, number: int=None) -> GameCenterLeaderboardsV2LinkageOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2LinkageOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterDetailGameCenterLeaderboardsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailGameCenterLeaderboardsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailGameCenterLeaderboardsV2LinkagesResponse.parse_obj(json)

    def update(self, request: GameCenterDetailGameCenterLeaderboardsV2LinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterDetailGameCenterLeaderboardsV2LinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class GameCenterLeaderboardsV2OfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/gameCenterLeaderboardsV2'

    def fields(self, *, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None) -> GameCenterLeaderboardsV2OfGameCenterDetailEndpoint:
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
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterDetailEndpoint
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

    def filter(self, *, reference_name: Union[str, list[str]]=None, archived: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterLeaderboardsV2OfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterDetailEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardsV2OfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, game_center_leaderboard_sets: int=None, versions: int=None) -> GameCenterLeaderboardsV2OfGameCenterDetailEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardsV2OfGameCenterDetailEndpoint
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

class LeaderboardReleasesLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/leaderboardReleases'

    def limit(self, number: int=None) -> LeaderboardReleasesLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardReleasesLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailLeaderboardReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailLeaderboardReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailLeaderboardReleasesLinkagesResponse.parse_obj(json)

class LeaderboardReleasesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/leaderboardReleases'

    def fields(self, *, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None) -> LeaderboardReleasesOfGameCenterDetailEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_release: the fields to include for returned resources of type gameCenterLeaderboardReleases
        :type game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardReleasesOfGameCenterDetailEndpoint
        '''
        if game_center_leaderboard_release: self._set_fields('gameCenterLeaderboardReleases',game_center_leaderboard_release if type(game_center_leaderboard_release) is list else [game_center_leaderboard_release])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_LEADERBOARD = 'gameCenterLeaderboard'

    def filter(self, *, live: Union[str, list[str]]=None, game_center_leaderboard: Union[str, list[str]]=None) -> LeaderboardReleasesOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param live: filter by attribute 'live'
        :type live: Union[str, list[str]] = None

        :param game_center_leaderboard: filter by id(s) of related 'gameCenterLeaderboard'
        :type game_center_leaderboard: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardReleasesOfGameCenterDetailEndpoint
        '''
        if live: self._set_filter('live', live if type(live) is list else [live])
        
        if game_center_leaderboard: self._set_filter('gameCenterLeaderboard', game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> LeaderboardReleasesOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LeaderboardReleasesOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LeaderboardReleasesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardReleasesOfGameCenterDetailEndpoint
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

class LeaderboardSetReleasesLinkagesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/relationships/leaderboardSetReleases'

    def limit(self, number: int=None) -> LeaderboardSetReleasesLinkagesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardSetReleasesLinkagesOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> GameCenterDetailLeaderboardSetReleasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterDetailLeaderboardSetReleasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailLeaderboardSetReleasesLinkagesResponse.parse_obj(json)

class LeaderboardSetReleasesOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/leaderboardSetReleases'

    def fields(self, *, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None) -> LeaderboardSetReleasesOfGameCenterDetailEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_release: the fields to include for returned resources of type gameCenterLeaderboardSetReleases
        :type game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardSetReleasesOfGameCenterDetailEndpoint
        '''
        if game_center_leaderboard_set_release: self._set_fields('gameCenterLeaderboardSetReleases',game_center_leaderboard_set_release if type(game_center_leaderboard_set_release) is list else [game_center_leaderboard_set_release])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_LEADERBOARD_SET = 'gameCenterLeaderboardSet'

    def filter(self, *, live: Union[str, list[str]]=None, game_center_leaderboard_set: Union[str, list[str]]=None) -> LeaderboardSetReleasesOfGameCenterDetailEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param live: filter by attribute 'live'
        :type live: Union[str, list[str]] = None

        :param game_center_leaderboard_set: filter by id(s) of related 'gameCenterLeaderboardSet'
        :type game_center_leaderboard_set: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardSetReleasesOfGameCenterDetailEndpoint
        '''
        if live: self._set_filter('live', live if type(live) is list else [live])
        
        if game_center_leaderboard_set: self._set_filter('gameCenterLeaderboardSet', game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> LeaderboardSetReleasesOfGameCenterDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.LeaderboardSetReleasesOfGameCenterDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> LeaderboardSetReleasesOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LeaderboardSetReleasesOfGameCenterDetailEndpoint
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

class ClassicMatchmakingRequestsOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/metrics/classicMatchmakingRequests'

    def sort(self, *, count: SortOrder=None, average_seconds_in_queue: SortOrder=None, p50_seconds_in_queue: SortOrder=None, p95_seconds_in_queue: SortOrder=None) -> ClassicMatchmakingRequestsOfGameCenterDetailEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.ClassicMatchmakingRequestsOfGameCenterDetailEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_seconds_in_queue: self.sort_expressions.append('averageSecondsInQueue' if average_seconds_in_queue == SortOrder.ASC else '-averageSecondsInQueue')
        if p50_seconds_in_queue: self.sort_expressions.append('p50SecondsInQueue' if p50_seconds_in_queue == SortOrder.ASC else '-p50SecondsInQueue')
        if p95_seconds_in_queue: self.sort_expressions.append('p95SecondsInQueue' if p95_seconds_in_queue == SortOrder.ASC else '-p95SecondsInQueue')
        return self
        
    def limit(self, number: int=None) -> ClassicMatchmakingRequestsOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ClassicMatchmakingRequestsOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingAppRequestsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingAppRequestsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingAppRequestsV1MetricResponse.parse_obj(json)

class RuleBasedMatchmakingRequestsOfGameCenterDetailEndpoint(IDEndpoint):
    path = '/v1/gameCenterDetails/{id}/metrics/ruleBasedMatchmakingRequests'

    def sort(self, *, count: SortOrder=None, average_seconds_in_queue: SortOrder=None, p50_seconds_in_queue: SortOrder=None, p95_seconds_in_queue: SortOrder=None) -> RuleBasedMatchmakingRequestsOfGameCenterDetailEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.RuleBasedMatchmakingRequestsOfGameCenterDetailEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_seconds_in_queue: self.sort_expressions.append('averageSecondsInQueue' if average_seconds_in_queue == SortOrder.ASC else '-averageSecondsInQueue')
        if p50_seconds_in_queue: self.sort_expressions.append('p50SecondsInQueue' if p50_seconds_in_queue == SortOrder.ASC else '-p50SecondsInQueue')
        if p95_seconds_in_queue: self.sort_expressions.append('p95SecondsInQueue' if p95_seconds_in_queue == SortOrder.ASC else '-p95SecondsInQueue')
        return self
        
    def limit(self, number: int=None) -> RuleBasedMatchmakingRequestsOfGameCenterDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.RuleBasedMatchmakingRequestsOfGameCenterDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingAppRequestsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingAppRequestsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingAppRequestsV1MetricResponse.parse_obj(json)

