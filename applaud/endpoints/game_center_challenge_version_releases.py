from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterChallengeVersionReleasesEndpoint(Endpoint):
    path = '/v1/gameCenterChallengeVersionReleases'

    @deprecated
    def create(self, request: GameCenterChallengeVersionReleaseCreateRequest) -> GameCenterChallengeVersionReleaseResponse:
        '''Create the resource.

        :param request: GameCenterChallengeVersionRelease representation
        :type request: GameCenterChallengeVersionReleaseCreateRequest

        :returns: Single GameCenterChallengeVersionRelease
        :rtype: GameCenterChallengeVersionReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterChallengeVersionReleaseResponse.parse_obj(json)

class GameCenterChallengeVersionReleaseEndpoint(IDEndpoint):
    path = '/v1/gameCenterChallengeVersionReleases/{id}'

    def fields(self, *, game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]]=None) -> GameCenterChallengeVersionReleaseEndpoint:
        '''Fields to return for included related types.

        :param game_center_challenge_version_release: the fields to include for returned resources of type gameCenterChallengeVersionReleases
        :type game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeVersionReleaseEndpoint
        '''
        if game_center_challenge_version_release: self._set_fields('gameCenterChallengeVersionReleases',game_center_challenge_version_release if type(game_center_challenge_version_release) is list else [game_center_challenge_version_release])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterChallengeVersionReleaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterChallengeVersionReleaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterChallengeVersionReleaseResponse:
        '''Get the resource.

        :returns: Single GameCenterChallengeVersionRelease
        :rtype: GameCenterChallengeVersionReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterChallengeVersionReleaseResponse.parse_obj(json)
    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

