from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterMatchmakingQueuesEndpoint(Endpoint):
    path = '/v1/gameCenterMatchmakingQueues'

    def fields(self, *, game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]]=None) -> GameCenterMatchmakingQueuesEndpoint:
        '''Fields to return for included related types.

        :param game_center_matchmaking_queue: the fields to include for returned resources of type gameCenterMatchmakingQueues
        :type game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingQueuesEndpoint
        '''
        if game_center_matchmaking_queue: self._set_fields('gameCenterMatchmakingQueues',game_center_matchmaking_queue if type(game_center_matchmaking_queue) is list else [game_center_matchmaking_queue])
        return self
        
    class Include(StringEnum):
        RULE_SET = 'ruleSet'
        EXPERIMENT_RULE_SET = 'experimentRuleSet'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterMatchmakingQueuesEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingQueuesEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> GameCenterMatchmakingQueuesEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingQueuesEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingQueuesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterMatchmakingQueues
        :rtype: GameCenterMatchmakingQueuesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingQueuesResponse.parse_obj(json)

    def create(self, request: GameCenterMatchmakingQueueCreateRequest) -> GameCenterMatchmakingQueueResponse:
        '''Create the resource.

        :param request: GameCenterMatchmakingQueue representation
        :type request: GameCenterMatchmakingQueueCreateRequest

        :returns: Single GameCenterMatchmakingQueue
        :rtype: GameCenterMatchmakingQueueResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterMatchmakingQueueResponse.parse_obj(json)

class GameCenterMatchmakingQueueEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingQueues/{id}'

    @endpoint('/v1/gameCenterMatchmakingQueues/{id}/metrics/experimentMatchmakingQueueSizes')
    def experiment_matchmaking_queue_sizes(self) -> ExperimentMatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint:
        return ExperimentMatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingQueues/{id}/metrics/experimentMatchmakingRequests')
    def experiment_matchmaking_requests(self) -> ExperimentMatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint:
        return ExperimentMatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingQueueSizes')
    def matchmaking_queue_sizes(self) -> MatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint:
        return MatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingRequests')
    def matchmaking_requests(self) -> MatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint:
        return MatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingSessions')
    def matchmaking_sessions(self) -> MatchmakingSessionsOfGameCenterMatchmakingQueueEndpoint:
        return MatchmakingSessionsOfGameCenterMatchmakingQueueEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]]=None) -> GameCenterMatchmakingQueueEndpoint:
        '''Fields to return for included related types.

        :param game_center_matchmaking_queue: the fields to include for returned resources of type gameCenterMatchmakingQueues
        :type game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingQueueEndpoint
        '''
        if game_center_matchmaking_queue: self._set_fields('gameCenterMatchmakingQueues',game_center_matchmaking_queue if type(game_center_matchmaking_queue) is list else [game_center_matchmaking_queue])
        return self
        
    class Include(StringEnum):
        RULE_SET = 'ruleSet'
        EXPERIMENT_RULE_SET = 'experimentRuleSet'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterMatchmakingQueueEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingQueueEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterMatchmakingQueueResponse:
        '''Get the resource.

        :returns: Single GameCenterMatchmakingQueue
        :rtype: GameCenterMatchmakingQueueResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingQueueResponse.parse_obj(json)

    def update(self, request: GameCenterMatchmakingQueueUpdateRequest) -> GameCenterMatchmakingQueueResponse:
        '''Modify the resource.

        :param request: GameCenterMatchmakingQueue representation
        :type request: GameCenterMatchmakingQueueUpdateRequest

        :returns: Single GameCenterMatchmakingQueue
        :rtype: GameCenterMatchmakingQueueResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterMatchmakingQueueResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class ExperimentMatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingQueues/{id}/metrics/experimentMatchmakingQueueSizes'

    def sort(self, *, count: SortOrder=None, average_number_of_request: SortOrder=None, p50_number_of_request: SortOrder=None, p95_number_of_request: SortOrder=None) -> ExperimentMatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.ExperimentMatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_number_of_request: self.sort_expressions.append('averageNumberOfRequests' if average_number_of_request == SortOrder.ASC else '-averageNumberOfRequests')
        if p50_number_of_request: self.sort_expressions.append('p50NumberOfRequests' if p50_number_of_request == SortOrder.ASC else '-p50NumberOfRequests')
        if p95_number_of_request: self.sort_expressions.append('p95NumberOfRequests' if p95_number_of_request == SortOrder.ASC else '-p95NumberOfRequests')
        return self
        
    def limit(self, number: int=None) -> ExperimentMatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ExperimentMatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingQueueSizesV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingQueueSizesV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingQueueSizesV1MetricResponse.parse_obj(json)

class ExperimentMatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingQueues/{id}/metrics/experimentMatchmakingRequests'

    def sort(self, *, count: SortOrder=None, average_seconds_in_queue: SortOrder=None, p50_seconds_in_queue: SortOrder=None, p95_seconds_in_queue: SortOrder=None) -> ExperimentMatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.ExperimentMatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_seconds_in_queue: self.sort_expressions.append('averageSecondsInQueue' if average_seconds_in_queue == SortOrder.ASC else '-averageSecondsInQueue')
        if p50_seconds_in_queue: self.sort_expressions.append('p50SecondsInQueue' if p50_seconds_in_queue == SortOrder.ASC else '-p50SecondsInQueue')
        if p95_seconds_in_queue: self.sort_expressions.append('p95SecondsInQueue' if p95_seconds_in_queue == SortOrder.ASC else '-p95SecondsInQueue')
        return self
        
    def limit(self, number: int=None) -> ExperimentMatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ExperimentMatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingQueueRequestsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingQueueRequestsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingQueueRequestsV1MetricResponse.parse_obj(json)

class MatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingQueueSizes'

    def sort(self, *, count: SortOrder=None, average_number_of_request: SortOrder=None, p50_number_of_request: SortOrder=None, p95_number_of_request: SortOrder=None) -> MatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.MatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_number_of_request: self.sort_expressions.append('averageNumberOfRequests' if average_number_of_request == SortOrder.ASC else '-averageNumberOfRequests')
        if p50_number_of_request: self.sort_expressions.append('p50NumberOfRequests' if p50_number_of_request == SortOrder.ASC else '-p50NumberOfRequests')
        if p95_number_of_request: self.sort_expressions.append('p95NumberOfRequests' if p95_number_of_request == SortOrder.ASC else '-p95NumberOfRequests')
        return self
        
    def limit(self, number: int=None) -> MatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingQueueSizesOfGameCenterMatchmakingQueueEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingQueueSizesV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingQueueSizesV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingQueueSizesV1MetricResponse.parse_obj(json)

class MatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingRequests'

    def sort(self, *, count: SortOrder=None, average_seconds_in_queue: SortOrder=None, p50_seconds_in_queue: SortOrder=None, p95_seconds_in_queue: SortOrder=None) -> MatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.MatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_seconds_in_queue: self.sort_expressions.append('averageSecondsInQueue' if average_seconds_in_queue == SortOrder.ASC else '-averageSecondsInQueue')
        if p50_seconds_in_queue: self.sort_expressions.append('p50SecondsInQueue' if p50_seconds_in_queue == SortOrder.ASC else '-p50SecondsInQueue')
        if p95_seconds_in_queue: self.sort_expressions.append('p95SecondsInQueue' if p95_seconds_in_queue == SortOrder.ASC else '-p95SecondsInQueue')
        return self
        
    def limit(self, number: int=None) -> MatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingRequestsOfGameCenterMatchmakingQueueEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingQueueRequestsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingQueueRequestsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingQueueRequestsV1MetricResponse.parse_obj(json)

class MatchmakingSessionsOfGameCenterMatchmakingQueueEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingSessions'

    def sort(self, *, count: SortOrder=None, average_player_count: SortOrder=None, p50_player_count: SortOrder=None, p95_player_count: SortOrder=None) -> MatchmakingSessionsOfGameCenterMatchmakingQueueEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.MatchmakingSessionsOfGameCenterMatchmakingQueueEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_player_count: self.sort_expressions.append('averagePlayerCount' if average_player_count == SortOrder.ASC else '-averagePlayerCount')
        if p50_player_count: self.sort_expressions.append('p50PlayerCount' if p50_player_count == SortOrder.ASC else '-p50PlayerCount')
        if p95_player_count: self.sort_expressions.append('p95PlayerCount' if p95_player_count == SortOrder.ASC else '-p95PlayerCount')
        return self
        
    def limit(self, number: int=None) -> MatchmakingSessionsOfGameCenterMatchmakingQueueEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingSessionsOfGameCenterMatchmakingQueueEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingSessionsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingSessionsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingSessionsV1MetricResponse.parse_obj(json)

