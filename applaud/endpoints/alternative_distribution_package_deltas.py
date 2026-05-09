from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AlternativeDistributionPackageDeltaEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackageDeltas/{id}'

    def fields(self, *, alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]]=None) -> AlternativeDistributionPackageDeltaEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package_delta: the fields to include for returned resources of type alternativeDistributionPackageDeltas
        :type alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageDeltaEndpoint
        '''
        if alternative_distribution_package_delta: self._set_fields('alternativeDistributionPackageDeltas',alternative_distribution_package_delta if type(alternative_distribution_package_delta) is list else [alternative_distribution_package_delta])
        return self
        
    def get(self) -> AlternativeDistributionPackageDeltaResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionPackageDelta
        :rtype: AlternativeDistributionPackageDeltaResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageDeltaResponse.parse_obj(json)

