from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterChallengesEndpoint(Endpoint):
    path = '/v1/gameCenterChallenges'

    def create(self, request: GameCenterChallengeCreateRequest) -> GameCenterChallengeResponse:
        '''Create the resource.

        :param request: GameCenterChallenge representation
        :type request: GameCenterChallengeCreateRequest

        :returns: Single GameCenterChallenge
        :rtype: GameCenterChallengeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterChallengeResponse.parse_obj(json)

class GameCenterChallengeEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallenges/{id}'

    @endpoint('/v1/gameCenterChallenges/{id}/versions')
    def versions(self) -> VersionsOfGameCenterChallengeEndpoint:
        return VersionsOfGameCenterChallengeEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterChallenges/{id}/relationships/leaderboard')
    def leaderboard_linkage(self) -> LeaderboardLinkageOfGameCenterChallengeEndpoint:
        return LeaderboardLinkageOfGameCenterChallengeEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterChallenges/{id}/relationships/leaderboardV2')
    def leaderboard_v2_linkage(self) -> LeaderboardV2LinkageOfGameCenterChallengeEndpoint:
        return LeaderboardV2LinkageOfGameCenterChallengeEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterChallenges/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfGameCenterChallengeEndpoint:
        return VersionsLinkagesOfGameCenterChallengeEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None) -> GameCenterChallengeEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :param game_center_challenge_version: the fields to include for returned resources of type gameCenterChallengeVersions
        :type game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeEndpoint
        '''
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        if game_center_challenge_version: self._set_fields('gameCenterChallengeVersions',game_center_challenge_version if type(game_center_challenge_version) is list else [game_center_challenge_version])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        VERSIONS = 'versions'
        LEADERBOARD = 'leaderboard'
        LEADERBOARD_V2 = 'leaderboardV2'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterChallengeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, versions: int=None) -> GameCenterChallengeEndpoint:
        '''Number of included related resources to return.

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeEndpoint
        '''
        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> GameCenterChallengeResponse:
        '''Get the resource.

        :returns: Single GameCenterChallenge
        :rtype: GameCenterChallengeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeResponse.parse_obj(json)

    def update(self, request: GameCenterChallengeUpdateRequest) -> GameCenterChallengeResponse:
        '''Modify the resource.

        :param request: GameCenterChallenge representation
        :type request: GameCenterChallengeUpdateRequest

        :returns: Single GameCenterChallenge
        :rtype: GameCenterChallengeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterChallengeResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class LeaderboardLinkageOfGameCenterChallengeEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallenges/{id}/relationships/leaderboard'

    @deprecated
    def update(self, request: GameCenterChallengeLeaderboardLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterChallengeLeaderboardLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class LeaderboardV2LinkageOfGameCenterChallengeEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallenges/{id}/relationships/leaderboardV2'

    def update(self, request: GameCenterChallengeLeaderboardV2LinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: GameCenterChallengeLeaderboardV2LinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class VersionsLinkagesOfGameCenterChallengeEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallenges/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfGameCenterChallengeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfGameCenterChallengeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterChallengeVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterChallengeVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeVersionsLinkagesResponse.parse_obj(json)

class VersionsOfGameCenterChallengeEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallenges/{id}/versions'

    def fields(self, *, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]]=None, game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]]=None, game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]]=None) -> VersionsOfGameCenterChallengeEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_version: the fields to include for returned resources of type gameCenterChallengeVersions
        :type game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]] = None

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :param game_center_challenge_localization: the fields to include for returned resources of type gameCenterChallengeLocalizations
        :type game_center_challenge_localization: Union[GameCenterChallengeLocalizationField, list[GameCenterChallengeLocalizationField]] = None

        :param game_center_challenge_version_release: the fields to include for returned resources of type gameCenterChallengeVersionReleases
        :type game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]] = None

        :param game_center_challenge_image: the fields to include for returned resources of type gameCenterChallengeImages
        :type game_center_challenge_image: Union[GameCenterChallengeImageField, list[GameCenterChallengeImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterChallengeEndpoint
        '''
        if game_center_challenge_version: self._set_fields('gameCenterChallengeVersions',game_center_challenge_version if type(game_center_challenge_version) is list else [game_center_challenge_version])
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        if game_center_challenge_localization: self._set_fields('gameCenterChallengeLocalizations',game_center_challenge_localization if type(game_center_challenge_localization) is list else [game_center_challenge_localization])
        if game_center_challenge_version_release: self._set_fields('gameCenterChallengeVersionReleases',game_center_challenge_version_release if type(game_center_challenge_version_release) is list else [game_center_challenge_version_release])
        if game_center_challenge_image: self._set_fields('gameCenterChallengeImages',game_center_challenge_image if type(game_center_challenge_image) is list else [game_center_challenge_image])
        return self
        
    class Include(StringEnum):
        CHALLENGE = 'challenge'
        LOCALIZATIONS = 'localizations'
        RELEASES = 'releases'
        DEFAULT_IMAGE = 'defaultImage'

    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfGameCenterChallengeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterChallengeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None, releases: int=None) -> VersionsOfGameCenterChallengeEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :param releases: maximum number of related releases returned (when they are included). The maximum limit is 50
        :type releases: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfGameCenterChallengeEndpoint
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

    def get(self) -> GameCenterChallengeVersionsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterChallengeVersions
        :rtype: GameCenterChallengeVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeVersionsResponse.parse_obj(json)

