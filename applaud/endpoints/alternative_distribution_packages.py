from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AlternativeDistributionPackagesEndpoint(Endpoint):
    path = '/v1/alternativeDistributionPackages'

    def create(self, request: AlternativeDistributionPackageCreateRequest) -> AlternativeDistributionPackageResponse:
        '''Create the resource.

        :param request: AlternativeDistributionPackage representation
        :type request: AlternativeDistributionPackageCreateRequest

        :returns: Single AlternativeDistributionPackage
        :rtype: AlternativeDistributionPackageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AlternativeDistributionPackageResponse.parse_obj(json)

class AlternativeDistributionPackageEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackages/{id}'

    @endpoint('/v1/alternativeDistributionPackages/{id}/versions')
    def versions(self) -> VersionsOfAlternativeDistributionPackageEndpoint:
        return VersionsOfAlternativeDistributionPackageEndpoint(self.id, self.session)
        
    @endpoint('/v1/alternativeDistributionPackages/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfAlternativeDistributionPackageEndpoint:
        return VersionsLinkagesOfAlternativeDistributionPackageEndpoint(self.id, self.session)
        
    def fields(self, *, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None, alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]]=None) -> AlternativeDistributionPackageEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package: the fields to include for returned resources of type alternativeDistributionPackages
        :type alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]] = None

        :param alternative_distribution_package_version: the fields to include for returned resources of type alternativeDistributionPackageVersions
        :type alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageEndpoint
        '''
        if alternative_distribution_package: self._set_fields('alternativeDistributionPackages',alternative_distribution_package if type(alternative_distribution_package) is list else [alternative_distribution_package])
        if alternative_distribution_package_version: self._set_fields('alternativeDistributionPackageVersions',alternative_distribution_package_version if type(alternative_distribution_package_version) is list else [alternative_distribution_package_version])
        return self
        
    class Include(StringEnum):
        VERSIONS = 'versions'

    def include(self, relationship: Union[Include, list[Include]]) -> AlternativeDistributionPackageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, versions: int=None) -> AlternativeDistributionPackageEndpoint:
        '''Number of included related resources to return.

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageEndpoint
        '''
        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> AlternativeDistributionPackageResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionPackage
        :rtype: AlternativeDistributionPackageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageResponse.parse_obj(json)

class VersionsLinkagesOfAlternativeDistributionPackageEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackages/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfAlternativeDistributionPackageEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfAlternativeDistributionPackageEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AlternativeDistributionPackageVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AlternativeDistributionPackageVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageVersionsLinkagesResponse.parse_obj(json)

class VersionsOfAlternativeDistributionPackageEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionPackages/{id}/versions'

    class State(StringEnum):
        COMPLETED = 'COMPLETED'
        REPLACED = 'REPLACED'

    def fields(self, *, alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]]=None, alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]]=None, alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]]=None, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None) -> VersionsOfAlternativeDistributionPackageEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package_version: the fields to include for returned resources of type alternativeDistributionPackageVersions
        :type alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]] = None

        :param alternative_distribution_package_variant: the fields to include for returned resources of type alternativeDistributionPackageVariants
        :type alternative_distribution_package_variant: Union[AlternativeDistributionPackageVariantField, list[AlternativeDistributionPackageVariantField]] = None

        :param alternative_distribution_package_delta: the fields to include for returned resources of type alternativeDistributionPackageDeltas
        :type alternative_distribution_package_delta: Union[AlternativeDistributionPackageDeltaField, list[AlternativeDistributionPackageDeltaField]] = None

        :param alternative_distribution_package: the fields to include for returned resources of type alternativeDistributionPackages
        :type alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfAlternativeDistributionPackageEndpoint
        '''
        if alternative_distribution_package_version: self._set_fields('alternativeDistributionPackageVersions',alternative_distribution_package_version if type(alternative_distribution_package_version) is list else [alternative_distribution_package_version])
        if alternative_distribution_package_variant: self._set_fields('alternativeDistributionPackageVariants',alternative_distribution_package_variant if type(alternative_distribution_package_variant) is list else [alternative_distribution_package_variant])
        if alternative_distribution_package_delta: self._set_fields('alternativeDistributionPackageDeltas',alternative_distribution_package_delta if type(alternative_distribution_package_delta) is list else [alternative_distribution_package_delta])
        if alternative_distribution_package: self._set_fields('alternativeDistributionPackages',alternative_distribution_package if type(alternative_distribution_package) is list else [alternative_distribution_package])
        return self
        
    class Include(StringEnum):
        VARIANTS = 'variants'
        DELTAS = 'deltas'
        ALTERNATIVE_DISTRIBUTION_PACKAGE = 'alternativeDistributionPackage'

    def filter(self, *, state: Union[State, list[State]]=None) -> VersionsOfAlternativeDistributionPackageEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfAlternativeDistributionPackageEndpoint
        '''
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfAlternativeDistributionPackageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfAlternativeDistributionPackageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, variants: int=None, deltas: int=None) -> VersionsOfAlternativeDistributionPackageEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param variants: maximum number of related variants returned (when they are included). The maximum limit is 50
        :type variants: int = None

        :param deltas: maximum number of related deltas returned (when they are included). The maximum limit is 50
        :type deltas: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfAlternativeDistributionPackageEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if variants and variants > 50:
            raise ValueError(f'The maximum limit of variants is 50')
        if variants: self._set_limit(variants, 'variants')

        if deltas and deltas > 50:
            raise ValueError(f'The maximum limit of deltas is 50')
        if deltas: self._set_limit(deltas, 'deltas')

        return self

    def get(self) -> AlternativeDistributionPackageVersionsResponse:
        '''Get one or more resources.

        :returns: List of AlternativeDistributionPackageVersions
        :rtype: AlternativeDistributionPackageVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageVersionsResponse.parse_obj(json)

