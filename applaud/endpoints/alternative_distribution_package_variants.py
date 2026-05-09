from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AlternativeDistributionPackageVariantEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackageVariants/{id}'

    def fields(self, *, alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]]=None) -> AlternativeDistributionPackageVariantEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package_variant: the fields to include for returned resources of type alternativeDistributionPackageVariants
        :type alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageVariantEndpoint
        '''
        if alternative_distribution_package_variant: self._set_fields('alternativeDistributionPackageVariants',alternative_distribution_package_variant if type(alternative_distribution_package_variant) is list else [alternative_distribution_package_variant])
        return self
        
    def get(self) -> AlternativeDistributionPackageVariantResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionPackageVariant
        :rtype: AlternativeDistributionPackageVariantResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageVariantResponse.parse_obj(json)

