from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ActorsEndpoint(Endpoint):
    path = '/v1/actors'

    def fields(self, *, actor: Union[ActorField, list[ActorField]]=None) -> ActorsEndpoint:
        '''Fields to return for included related types.

        :param actor: the fields to include for returned resources of type actors
        :type actor: Union[ActorField, list[ActorField]] = None

        :returns: self
        :rtype: applaud.endpoints.ActorsEndpoint
        '''
        if actor: self._set_fields('actors',actor if type(actor) is list else [actor])
        return self
        
    def filter(self, *, id: Union[str, list[str]]) -> ActorsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]]

        :returns: self
        :rtype: applaud.endpoints.ActorsEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def limit(self, number: int=None) -> ActorsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ActorsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ActorsResponse:
        '''Get one or more resources.

        :returns: List of Actors
        :rtype: ActorsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ActorsResponse.parse_obj(json)

class ActorEndpoint(IDEndpoint):
    path = '/v1/actors/{id}'

    def fields(self, *, actor: Union[ActorField, list[ActorField]]=None) -> ActorEndpoint:
        '''Fields to return for included related types.

        :param actor: the fields to include for returned resources of type actors
        :type actor: Union[ActorField, list[ActorField]] = None

        :returns: self
        :rtype: applaud.endpoints.ActorEndpoint
        '''
        if actor: self._set_fields('actors',actor if type(actor) is list else [actor])
        return self
        
    def get(self) -> ActorResponse:
        '''Get the resource.

        :returns: Single Actor
        :rtype: ActorResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ActorResponse.parse_obj(json)

