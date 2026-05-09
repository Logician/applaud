from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AlternativeDistributionPackageVersionEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackageVersions/{id}'

    @endpoint('/v1/alternativeDistributionPackageVersions/{id}/deltas')
    def deltas(self) -> DeltasOfAlternativeDistributionPackageVersionEndpoint:
        return DeltasOfAlternativeDistributionPackageVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/alternativeDistributionPackageVersions/{id}/variants')
    def variants(self) -> VariantsOfAlternativeDistributionPackageVersionEndpoint:
        return VariantsOfAlternativeDistributionPackageVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/alternativeDistributionPackageVersions/{id}/relationships/deltas')
    def deltas_linkages(self) -> DeltasLinkagesOfAlternativeDistributionPackageVersionEndpoint:
        return DeltasLinkagesOfAlternativeDistributionPackageVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/alternativeDistributionPackageVersions/{id}/relationships/variants')
    def variants_linkages(self) -> VariantsLinkagesOfAlternativeDistributionPackageVersionEndpoint:
        return VariantsLinkagesOfAlternativeDistributionPackageVersionEndpoint(self.id, self.session)
        
    def fields(self, *, alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]]=None, alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]]=None, alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]]=None) -> AlternativeDistributionPackageVersionEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package_version: the fields to include for returned resources of type alternativeDistributionPackageVersions
        :type alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]] = None

        :param alternative_distribution_package_variant: the fields to include for returned resources of type alternativeDistributionPackageVariants
        :type alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]] = None

        :param alternative_distribution_package_delta: the fields to include for returned resources of type alternativeDistributionPackageDeltas
        :type alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageVersionEndpoint
        '''
        if alternative_distribution_package_version: self._set_fields('alternativeDistributionPackageVersions',alternative_distribution_package_version if type(alternative_distribution_package_version) is list else [alternative_distribution_package_version])
        if alternative_distribution_package_variant: self._set_fields('alternativeDistributionPackageVariants',alternative_distribution_package_variant if type(alternative_distribution_package_variant) is list else [alternative_distribution_package_variant])
        if alternative_distribution_package_delta: self._set_fields('alternativeDistributionPackageDeltas',alternative_distribution_package_delta if type(alternative_distribution_package_delta) is list else [alternative_distribution_package_delta])
        return self
        
    class Include(StringEnum):
        VARIANTS = 'variants'
        DELTAS = 'deltas'
        ALTERNATIVE_DISTRIBUTION_PACKAGE = 'alternativeDistributionPackage'

    def include(self, relationship: Union[Include, list[Include]]) -> AlternativeDistributionPackageVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, deltas: int=None, variants: int=None) -> AlternativeDistributionPackageVersionEndpoint:
        '''Number of included related resources to return.

        :param deltas: maximum number of related deltas returned (when they are included). The maximum limit is 50
        :type deltas: int = None

        :param variants: maximum number of related variants returned (when they are included). The maximum limit is 50
        :type variants: int = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageVersionEndpoint
        '''
        if deltas and deltas > 50:
            raise ValueError(f'The maximum limit of deltas is 50')
        if deltas: self._set_limit(deltas, 'deltas')

        if variants and variants > 50:
            raise ValueError(f'The maximum limit of variants is 50')
        if variants: self._set_limit(variants, 'variants')

        return self

    def get(self) -> AlternativeDistributionPackageVersionResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionPackageVersion
        :rtype: AlternativeDistributionPackageVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageVersionResponse.parse_obj(json)

class DeltasLinkagesOfAlternativeDistributionPackageVersionEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackageVersions/{id}/relationships/deltas'

    def limit(self, number: int=None) -> DeltasLinkagesOfAlternativeDistributionPackageVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DeltasLinkagesOfAlternativeDistributionPackageVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AlternativeDistributionPackageVersionDeltasLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AlternativeDistributionPackageVersionDeltasLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageVersionDeltasLinkagesResponse.parse_obj(json)

class DeltasOfAlternativeDistributionPackageVersionEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackageVersions/{id}/deltas'

    def fields(self, *, alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]]=None) -> DeltasOfAlternativeDistributionPackageVersionEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package_delta: the fields to include for returned resources of type alternativeDistributionPackageDeltas
        :type alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]] = None

        :returns: self
        :rtype: applaud.endpoints.DeltasOfAlternativeDistributionPackageVersionEndpoint
        '''
        if alternative_distribution_package_delta: self._set_fields('alternativeDistributionPackageDeltas',alternative_distribution_package_delta if type(alternative_distribution_package_delta) is list else [alternative_distribution_package_delta])
        return self
        
    def limit(self, number: int=None) -> DeltasOfAlternativeDistributionPackageVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DeltasOfAlternativeDistributionPackageVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AlternativeDistributionPackageDeltasResponse:
        '''Get one or more resources.

        :returns: List of AlternativeDistributionPackageDeltas
        :rtype: AlternativeDistributionPackageDeltasResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageDeltasResponse.parse_obj(json)

class VariantsLinkagesOfAlternativeDistributionPackageVersionEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackageVersions/{id}/relationships/variants'

    def limit(self, number: int=None) -> VariantsLinkagesOfAlternativeDistributionPackageVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VariantsLinkagesOfAlternativeDistributionPackageVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AlternativeDistributionPackageVersionVariantsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AlternativeDistributionPackageVersionVariantsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageVersionVariantsLinkagesResponse.parse_obj(json)

class VariantsOfAlternativeDistributionPackageVersionEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackageVersions/{id}/variants'

    def fields(self, *, alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]]=None) -> VariantsOfAlternativeDistributionPackageVersionEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package_variant: the fields to include for returned resources of type alternativeDistributionPackageVariants
        :type alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]] = None

        :returns: self
        :rtype: applaud.endpoints.VariantsOfAlternativeDistributionPackageVersionEndpoint
        '''
        if alternative_distribution_package_variant: self._set_fields('alternativeDistributionPackageVariants',alternative_distribution_package_variant if type(alternative_distribution_package_variant) is list else [alternative_distribution_package_variant])
        return self
        
    def limit(self, number: int=None) -> VariantsOfAlternativeDistributionPackageVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VariantsOfAlternativeDistributionPackageVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AlternativeDistributionPackageVariantsResponse:
        '''Get one or more resources.

        :returns: List of AlternativeDistributionPackageVariants
        :rtype: AlternativeDistributionPackageVariantsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageVariantsResponse.parse_obj(json)

