from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SandboxTestersEndpoint(Endpoint):
    path = '/v2/sandboxTesters'

    def fields(self, *, sandbox_tester: Union[SandboxTesterField, list[SandboxTesterField]]=None) -> SandboxTestersEndpoint:
        '''Fields to return for included related types.

        :param sandbox_tester: the fields to include for returned resources of type sandboxTesters
        :type sandbox_tester: Union[SandboxTesterField, list[SandboxTesterField]] = None

        :returns: self
        :rtype: applaud.endpoints.SandboxTestersEndpoint
        '''
        if sandbox_tester: self._set_fields('sandboxTesters',sandbox_tester if type(sandbox_tester) is list else [sandbox_tester])
        return self
        
    def limit(self, number: int=None) -> SandboxTestersEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SandboxTestersEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SandboxTestersV2Response:
        '''Get one or more resources.

        :returns: List of SandboxTesters
        :rtype: SandboxTestersV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SandboxTestersV2Response.parse_obj(json)

class SandboxTesterEndpoint(IDEndpoint):
    path = '/v2/sandboxTesters/{id}'

    def update(self, request: SandboxTesterV2UpdateRequest) -> SandboxTesterV2Response:
        '''Modify the resource.

        :param request: SandboxTester representation
        :type request: SandboxTesterV2UpdateRequest

        :returns: Single SandboxTester
        :rtype: SandboxTesterV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SandboxTesterV2Response.parse_obj(json)

