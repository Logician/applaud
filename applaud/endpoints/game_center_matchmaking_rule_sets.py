from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterMatchmakingRuleSetsEndpoint(Endpoint):
    path = '/v1/gameCenterMatchmakingRuleSets'

    def fields(self, *, game_center_matchmaking_rule_set: Union[GameCenterMatchmakingRuleSetField, list[GameCenterMatchmakingRuleSetField]]=None, game_center_matchmaking_team: Union[GameCenterMatchmakingTeamField, list[GameCenterMatchmakingTeamField]]=None, game_center_matchmaking_rule: Union[GameCenterMatchmakingRuleField, list[GameCenterMatchmakingRuleField]]=None, game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]]=None) -> GameCenterMatchmakingRuleSetsEndpoint:
        '''Fields to return for included related types.

        :param game_center_matchmaking_rule_set: the fields to include for returned resources of type gameCenterMatchmakingRuleSets
        :type game_center_matchmaking_rule_set: Union[GameCenterMatchmakingRuleSetField, list[GameCenterMatchmakingRuleSetField]] = None

        :param game_center_matchmaking_team: the fields to include for returned resources of type gameCenterMatchmakingTeams
        :type game_center_matchmaking_team: Union[GameCenterMatchmakingTeamField, list[GameCenterMatchmakingTeamField]] = None

        :param game_center_matchmaking_rule: the fields to include for returned resources of type gameCenterMatchmakingRules
        :type game_center_matchmaking_rule: Union[GameCenterMatchmakingRuleField, list[GameCenterMatchmakingRuleField]] = None

        :param game_center_matchmaking_queue: the fields to include for returned resources of type gameCenterMatchmakingQueues
        :type game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingRuleSetsEndpoint
        '''
        if game_center_matchmaking_rule_set: self._set_fields('gameCenterMatchmakingRuleSets',game_center_matchmaking_rule_set if type(game_center_matchmaking_rule_set) is list else [game_center_matchmaking_rule_set])
        if game_center_matchmaking_team: self._set_fields('gameCenterMatchmakingTeams',game_center_matchmaking_team if type(game_center_matchmaking_team) is list else [game_center_matchmaking_team])
        if game_center_matchmaking_rule: self._set_fields('gameCenterMatchmakingRules',game_center_matchmaking_rule if type(game_center_matchmaking_rule) is list else [game_center_matchmaking_rule])
        if game_center_matchmaking_queue: self._set_fields('gameCenterMatchmakingQueues',game_center_matchmaking_queue if type(game_center_matchmaking_queue) is list else [game_center_matchmaking_queue])
        return self
        
    class Include(StringEnum):
        TEAMS = 'teams'
        RULES = 'rules'
        MATCHMAKING_QUEUES = 'matchmakingQueues'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterMatchmakingRuleSetsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingRuleSetsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, matchmaking_queues: int=None, rules: int=None, teams: int=None) -> GameCenterMatchmakingRuleSetsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param matchmaking_queues: maximum number of related matchmakingQueues returned (when they are included). The maximum limit is 50
        :type matchmaking_queues: int = None

        :param rules: maximum number of related rules returned (when they are included). The maximum limit is 50
        :type rules: int = None

        :param teams: maximum number of related teams returned (when they are included). The maximum limit is 50
        :type teams: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingRuleSetsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if matchmaking_queues and matchmaking_queues > 50:
            raise ValueError(f'The maximum limit of matchmaking_queues is 50')
        if matchmaking_queues: self._set_limit(matchmaking_queues, 'matchmakingQueues')

        if rules and rules > 50:
            raise ValueError(f'The maximum limit of rules is 50')
        if rules: self._set_limit(rules, 'rules')

        if teams and teams > 50:
            raise ValueError(f'The maximum limit of teams is 50')
        if teams: self._set_limit(teams, 'teams')

        return self

    def get(self) -> GameCenterMatchmakingRuleSetsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterMatchmakingRuleSets
        :rtype: GameCenterMatchmakingRuleSetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingRuleSetsResponse.parse_obj(json)

    def create(self, request: GameCenterMatchmakingRuleSetCreateRequest) -> GameCenterMatchmakingRuleSetResponse:
        '''Create the resource.

        :param request: GameCenterMatchmakingRuleSet representation
        :type request: GameCenterMatchmakingRuleSetCreateRequest

        :returns: Single GameCenterMatchmakingRuleSet
        :rtype: GameCenterMatchmakingRuleSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterMatchmakingRuleSetResponse.parse_obj(json)

class GameCenterMatchmakingRuleSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRuleSets/{id}'

    @endpoint('/v1/gameCenterMatchmakingRuleSets/{id}/matchmakingQueues')
    def matchmaking_queues(self) -> MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint:
        return MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingRuleSets/{id}/rules')
    def rules(self) -> RulesOfGameCenterMatchmakingRuleSetEndpoint:
        return RulesOfGameCenterMatchmakingRuleSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingRuleSets/{id}/teams')
    def teams(self) -> TeamsOfGameCenterMatchmakingRuleSetEndpoint:
        return TeamsOfGameCenterMatchmakingRuleSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingRuleSets/{id}/relationships/matchmakingQueues')
    def matchmaking_queues_linkages(self) -> MatchmakingQueuesLinkagesOfGameCenterMatchmakingRuleSetEndpoint:
        return MatchmakingQueuesLinkagesOfGameCenterMatchmakingRuleSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingRuleSets/{id}/relationships/rules')
    def rules_linkages(self) -> RulesLinkagesOfGameCenterMatchmakingRuleSetEndpoint:
        return RulesLinkagesOfGameCenterMatchmakingRuleSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterMatchmakingRuleSets/{id}/relationships/teams')
    def teams_linkages(self) -> TeamsLinkagesOfGameCenterMatchmakingRuleSetEndpoint:
        return TeamsLinkagesOfGameCenterMatchmakingRuleSetEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_matchmaking_rule_set: Union[GameCenterMatchmakingRuleSetField, list[GameCenterMatchmakingRuleSetField]]=None, game_center_matchmaking_team: Union[GameCenterMatchmakingTeamField, list[GameCenterMatchmakingTeamField]]=None, game_center_matchmaking_rule: Union[GameCenterMatchmakingRuleField, list[GameCenterMatchmakingRuleField]]=None, game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]]=None) -> GameCenterMatchmakingRuleSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_matchmaking_rule_set: the fields to include for returned resources of type gameCenterMatchmakingRuleSets
        :type game_center_matchmaking_rule_set: Union[GameCenterMatchmakingRuleSetField, list[GameCenterMatchmakingRuleSetField]] = None

        :param game_center_matchmaking_team: the fields to include for returned resources of type gameCenterMatchmakingTeams
        :type game_center_matchmaking_team: Union[GameCenterMatchmakingTeamField, list[GameCenterMatchmakingTeamField]] = None

        :param game_center_matchmaking_rule: the fields to include for returned resources of type gameCenterMatchmakingRules
        :type game_center_matchmaking_rule: Union[GameCenterMatchmakingRuleField, list[GameCenterMatchmakingRuleField]] = None

        :param game_center_matchmaking_queue: the fields to include for returned resources of type gameCenterMatchmakingQueues
        :type game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingRuleSetEndpoint
        '''
        if game_center_matchmaking_rule_set: self._set_fields('gameCenterMatchmakingRuleSets',game_center_matchmaking_rule_set if type(game_center_matchmaking_rule_set) is list else [game_center_matchmaking_rule_set])
        if game_center_matchmaking_team: self._set_fields('gameCenterMatchmakingTeams',game_center_matchmaking_team if type(game_center_matchmaking_team) is list else [game_center_matchmaking_team])
        if game_center_matchmaking_rule: self._set_fields('gameCenterMatchmakingRules',game_center_matchmaking_rule if type(game_center_matchmaking_rule) is list else [game_center_matchmaking_rule])
        if game_center_matchmaking_queue: self._set_fields('gameCenterMatchmakingQueues',game_center_matchmaking_queue if type(game_center_matchmaking_queue) is list else [game_center_matchmaking_queue])
        return self
        
    class Include(StringEnum):
        TEAMS = 'teams'
        RULES = 'rules'
        MATCHMAKING_QUEUES = 'matchmakingQueues'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterMatchmakingRuleSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingRuleSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, matchmaking_queues: int=None, rules: int=None, teams: int=None) -> GameCenterMatchmakingRuleSetEndpoint:
        '''Number of included related resources to return.

        :param matchmaking_queues: maximum number of related matchmakingQueues returned (when they are included). The maximum limit is 50
        :type matchmaking_queues: int = None

        :param rules: maximum number of related rules returned (when they are included). The maximum limit is 50
        :type rules: int = None

        :param teams: maximum number of related teams returned (when they are included). The maximum limit is 50
        :type teams: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterMatchmakingRuleSetEndpoint
        '''
        if matchmaking_queues and matchmaking_queues > 50:
            raise ValueError(f'The maximum limit of matchmaking_queues is 50')
        if matchmaking_queues: self._set_limit(matchmaking_queues, 'matchmakingQueues')

        if rules and rules > 50:
            raise ValueError(f'The maximum limit of rules is 50')
        if rules: self._set_limit(rules, 'rules')

        if teams and teams > 50:
            raise ValueError(f'The maximum limit of teams is 50')
        if teams: self._set_limit(teams, 'teams')

        return self

    def get(self) -> GameCenterMatchmakingRuleSetResponse:
        '''Get the resource.

        :returns: Single GameCenterMatchmakingRuleSet
        :rtype: GameCenterMatchmakingRuleSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingRuleSetResponse.parse_obj(json)

    def update(self, request: GameCenterMatchmakingRuleSetUpdateRequest) -> GameCenterMatchmakingRuleSetResponse:
        '''Modify the resource.

        :param request: GameCenterMatchmakingRuleSet representation
        :type request: GameCenterMatchmakingRuleSetUpdateRequest

        :returns: Single GameCenterMatchmakingRuleSet
        :rtype: GameCenterMatchmakingRuleSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterMatchmakingRuleSetResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class MatchmakingQueuesLinkagesOfGameCenterMatchmakingRuleSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRuleSets/{id}/relationships/matchmakingQueues'

    def limit(self, number: int=None) -> MatchmakingQueuesLinkagesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingQueuesLinkagesOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingRuleSetMatchmakingQueuesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterMatchmakingRuleSetMatchmakingQueuesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingRuleSetMatchmakingQueuesLinkagesResponse.parse_obj(json)

class MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRuleSets/{id}/matchmakingQueues'

    def fields(self, *, game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]]=None, game_center_matchmaking_rule_set: Union[GameCenterMatchmakingRuleSetField, list[GameCenterMatchmakingRuleSetField]]=None) -> MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_matchmaking_queue: the fields to include for returned resources of type gameCenterMatchmakingQueues
        :type game_center_matchmaking_queue: Union[GameCenterMatchmakingQueueField, list[GameCenterMatchmakingQueueField]] = None

        :param game_center_matchmaking_rule_set: the fields to include for returned resources of type gameCenterMatchmakingRuleSets
        :type game_center_matchmaking_rule_set: Union[GameCenterMatchmakingRuleSetField, list[GameCenterMatchmakingRuleSetField]] = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if game_center_matchmaking_queue: self._set_fields('gameCenterMatchmakingQueues',game_center_matchmaking_queue if type(game_center_matchmaking_queue) is list else [game_center_matchmaking_queue])
        if game_center_matchmaking_rule_set: self._set_fields('gameCenterMatchmakingRuleSets',game_center_matchmaking_rule_set if type(game_center_matchmaking_rule_set) is list else [game_center_matchmaking_rule_set])
        return self
        
    class Include(StringEnum):
        RULE_SET = 'ruleSet'
        EXPERIMENT_RULE_SET = 'experimentRuleSet'

    def include(self, relationship: Union[Include, list[Include]]) -> MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MatchmakingQueuesOfGameCenterMatchmakingRuleSetEndpoint
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

class RulesLinkagesOfGameCenterMatchmakingRuleSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRuleSets/{id}/relationships/rules'

    def limit(self, number: int=None) -> RulesLinkagesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.RulesLinkagesOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingRuleSetRulesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterMatchmakingRuleSetRulesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingRuleSetRulesLinkagesResponse.parse_obj(json)

class RulesOfGameCenterMatchmakingRuleSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRuleSets/{id}/rules'

    def fields(self, *, game_center_matchmaking_rule: Union[GameCenterMatchmakingRuleField, list[GameCenterMatchmakingRuleField]]=None) -> RulesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_matchmaking_rule: the fields to include for returned resources of type gameCenterMatchmakingRules
        :type game_center_matchmaking_rule: Union[GameCenterMatchmakingRuleField, list[GameCenterMatchmakingRuleField]] = None

        :returns: self
        :rtype: applaud.endpoints.RulesOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if game_center_matchmaking_rule: self._set_fields('gameCenterMatchmakingRules',game_center_matchmaking_rule if type(game_center_matchmaking_rule) is list else [game_center_matchmaking_rule])
        return self
        
    def limit(self, number: int=None) -> RulesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.RulesOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingRulesResponse:
        '''Get one or more resources.

        :returns: List of GameCenterMatchmakingRules
        :rtype: GameCenterMatchmakingRulesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingRulesResponse.parse_obj(json)

class TeamsLinkagesOfGameCenterMatchmakingRuleSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRuleSets/{id}/relationships/teams'

    def limit(self, number: int=None) -> TeamsLinkagesOfGameCenterMatchmakingRuleSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TeamsLinkagesOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingRuleSetTeamsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterMatchmakingRuleSetTeamsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingRuleSetTeamsLinkagesResponse.parse_obj(json)

class TeamsOfGameCenterMatchmakingRuleSetEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingRuleSets/{id}/teams'

    def fields(self, *, game_center_matchmaking_team: Union[GameCenterMatchmakingTeamField, list[GameCenterMatchmakingTeamField]]=None) -> TeamsOfGameCenterMatchmakingRuleSetEndpoint:
        '''Fields to return for included related types.

        :param game_center_matchmaking_team: the fields to include for returned resources of type gameCenterMatchmakingTeams
        :type game_center_matchmaking_team: Union[GameCenterMatchmakingTeamField, list[GameCenterMatchmakingTeamField]] = None

        :returns: self
        :rtype: applaud.endpoints.TeamsOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if game_center_matchmaking_team: self._set_fields('gameCenterMatchmakingTeams',game_center_matchmaking_team if type(game_center_matchmaking_team) is list else [game_center_matchmaking_team])
        return self
        
    def limit(self, number: int=None) -> TeamsOfGameCenterMatchmakingRuleSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TeamsOfGameCenterMatchmakingRuleSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterMatchmakingTeamsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterMatchmakingTeams
        :rtype: GameCenterMatchmakingTeamsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterMatchmakingTeamsResponse.parse_obj(json)

