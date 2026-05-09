from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaCrashLogEndpoint(IDEndpoint):
    path = '/v1/betaCrashLogs/{id}'

    def fields(self, *, beta_crash_log: Union[BetaCrashLogField, list[BetaCrashLogField]]=None) -> BetaCrashLogEndpoint:
        '''Fields to return for included related types.

        :param beta_crash_log: the fields to include for returned resources of type betaCrashLogs
        :type beta_crash_log: Union[BetaCrashLogField, list[BetaCrashLogField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaCrashLogEndpoint
        '''
        if beta_crash_log: self._set_fields('betaCrashLogs',beta_crash_log if type(beta_crash_log) is list else [beta_crash_log])
        return self
        
    def get(self) -> BetaCrashLogResponse:
        '''Get the resource.

        :returns: Single BetaCrashLog
        :rtype: BetaCrashLogResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaCrashLogResponse.parse_obj(json)

