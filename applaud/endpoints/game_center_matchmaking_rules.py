from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterMatchmakingRulesEndpoint(Endpoint):
    path = '/v1/gameCenterMatchmakingRules'

    def create(self, request: GameCenterMatchmakingRuleCreateRequest) -> GameCenterMatchmakingRuleResponse:
        '''Create the resource.

        :param request: GameCenterMatchmakingRule representation
        :type request: GameCenterMatchmakingRuleCreateRequest

        :returns: Single GameCenterMatchmakingRule
        :rtype: GameCenterMatchmakingRuleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterMatchmakingRuleResponse.parse_obj(json)

class GameCenterMatchmakingRuleEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRules/{id}'

    @endpoint('/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingBooleanRuleResults')
    def matchmaking_boolean_rule_results(self) -> MatchmakingBooleanRuleResultsOfGameCenterMatchmakingRuleEndpoint:
        return MatchmakingBooleanRuleResultsOfGameCenterMatchmakingRuleEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingNumberRuleResults')
    def matchmaking_number_rule_results(self) -> MatchmakingNumberRuleResultsOfGameCenterMatchmakingRuleEndpoint:
        return MatchmakingNumberRuleResultsOfGameCenterMatchmakingRuleEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingRuleErrors')
    def matchmaking_rule_errors(self) -> MatchmakingRuleErrorsOfGameCenterMatchmakingRuleEndpoint:
        return MatchmakingRuleErrorsOfGameCenterMatchmakingRuleEndpoint(self.id, self.session)
        
    def update(self, request: GameCenterMatchmakingRuleUpdateRequest) -> GameCenterMatchmakingRuleResponse:
        '''Modify the resource.

        :param request: GameCenterMatchmakingRule representation
        :type request: GameCenterMatchmakingRuleUpdateRequest

        :returns: Single GameCenterMatchmakingRule
        :rtype: GameCenterMatchmakingRuleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterMatchmakingRuleResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class MatchmakingBooleanRuleResultsOfGameCenterMatchmakingRuleEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingBooleanRuleResults'

    def sort(self, *, count: SortOrder=None) -> MatchmakingBooleanRuleResultsOfGameCenterMatchmakingRuleEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.MatchmakingBooleanRuleResultsOfGameCenterMatchmakingRuleEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        return self
        
    def limit(self, number: int=None) -> MatchmakingBooleanRuleResultsOfGameCenterMatchmakingRuleEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingBooleanRuleResultsOfGameCenterMatchmakingRuleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingBooleanRuleResultsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingBooleanRuleResultsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingBooleanRuleResultsV1MetricResponse.parse_obj(json)

class MatchmakingNumberRuleResultsOfGameCenterMatchmakingRuleEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingNumberRuleResults'

    def sort(self, *, count: SortOrder=None, average_result: SortOrder=None, p50_result: SortOrder=None, p95_result: SortOrder=None) -> MatchmakingNumberRuleResultsOfGameCenterMatchmakingRuleEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.MatchmakingNumberRuleResultsOfGameCenterMatchmakingRuleEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        if average_result: self.sort_expressions.append('averageResult' if average_result == SortOrder.ASC else '-averageResult')
        if p50_result: self.sort_expressions.append('p50Result' if p50_result == SortOrder.ASC else '-p50Result')
        if p95_result: self.sort_expressions.append('p95Result' if p95_result == SortOrder.ASC else '-p95Result')
        return self
        
    def limit(self, number: int=None) -> MatchmakingNumberRuleResultsOfGameCenterMatchmakingRuleEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingNumberRuleResultsOfGameCenterMatchmakingRuleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingNumberRuleResultsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingNumberRuleResultsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingNumberRuleResultsV1MetricResponse.parse_obj(json)

class MatchmakingRuleErrorsOfGameCenterMatchmakingRuleEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingRuleErrors'

    def sort(self, *, count: SortOrder=None) -> MatchmakingRuleErrorsOfGameCenterMatchmakingRuleEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.MatchmakingRuleErrorsOfGameCenterMatchmakingRuleEndpoint
        '''
        if count: self.sort_expressions.append('count' if count == SortOrder.ASC else '-count')
        return self
        
    def limit(self, number: int=None) -> MatchmakingRuleErrorsOfGameCenterMatchmakingRuleEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingRuleErrorsOfGameCenterMatchmakingRuleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingRuleErrorsV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: GameCenterMatchmakingRuleErrorsV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingRuleErrorsV1MetricResponse.parse_obj(json)

