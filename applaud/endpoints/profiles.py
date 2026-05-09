from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ProfilesEndpoint(Endpoint):
    path = '/v1/profiles'

    def fields(self, *, profile: Union[ProfileField, list[ProfileField]]=None, bundle_id: Union[BundleIdField, list[BundleIdField]]=None, device: Union[DeviceField, list[DeviceField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None) -> ProfilesEndpoint:
        '''Fields to return for included related types.

        :param profile: the fields to include for returned resources of type profiles
        :type profile: Union[ProfileField, list[ProfileField]] = None

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if profile: self._set_fields('profiles',profile if type(profile) is list else [profile])
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        if device: self._set_fields('devices',device if type(device) is list else [device])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    class Include(StringEnum):
        BUNDLE_ID = 'bundleId'
        DEVICES = 'devices'
        CERTIFICATES = 'certificates'

    def filter(self, *, name: Union[str, list[str]]=None, profile_type: Union[ProfileType, list[ProfileType]]=None, profile_state: Union[ProfileState, list[ProfileState]]=None, id: Union[str, list[str]]=None) -> ProfilesEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param profile_type: filter by attribute 'profileType'
        :type profile_type: Union[ProfileType, list[ProfileType]] = None

        :param profile_state: filter by attribute 'profileState'
        :type profile_state: Union[ProfileState, list[ProfileState]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if profile_type: self._set_filter('profileType', profile_type if type(profile_type) is list else [profile_type])
        
        if profile_state: self._set_filter('profileState', profile_state if type(profile_state) is list else [profile_state])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ProfilesEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None, profile_type: SortOrder=None, profile_state: SortOrder=None, id: SortOrder=None) -> ProfilesEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if profile_type: self.sort_expressions.append('profileType' if profile_type == SortOrder.ASC else '-profileType')
        if profile_state: self.sort_expressions.append('profileState' if profile_state == SortOrder.ASC else '-profileState')
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        return self
        
    def limit(self, number: int=None, *, certificates: int=None, devices: int=None) -> ProfilesEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :param devices: maximum number of related devices returned (when they are included). The maximum limit is 50
        :type devices: int = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit of certificates is 50')
        if certificates: self._set_limit(certificates, 'certificates')

        if devices and devices > 50:
            raise ValueError(f'The maximum limit of devices is 50')
        if devices: self._set_limit(devices, 'devices')

        return self

    def get(self) -> ProfilesResponse:
        '''Get one or more resources.

        :returns: List of Profiles
        :rtype: ProfilesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfilesResponse.parse_obj(json)

    def create(self, request: ProfileCreateRequest) -> ProfileResponse:
        '''Create the resource.

        :param request: Profile representation
        :type request: ProfileCreateRequest

        :returns: Single Profile
        :rtype: ProfileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return ProfileResponse.parse_obj(json)

class ProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}'

    @endpoint('/v1/profiles/{id}/bundleId')
    def bundle_id(self) -> BundleIdOfProfileEndpoint:
        return BundleIdOfProfileEndpoint(self.id, self.session)
        
    @endpoint('/v1/profiles/{id}/certificates')
    def certificates(self) -> CertificatesOfProfileEndpoint:
        return CertificatesOfProfileEndpoint(self.id, self.session)
        
    @endpoint('/v1/profiles/{id}/devices')
    def devices(self) -> DevicesOfProfileEndpoint:
        return DevicesOfProfileEndpoint(self.id, self.session)
        
    @endpoint('/v1/profiles/{id}/relationships/bundleId')
    def bundle_id_linkage(self) -> BundleIdLinkageOfProfileEndpoint:
        return BundleIdLinkageOfProfileEndpoint(self.id, self.session)
        
    @endpoint('/v1/profiles/{id}/relationships/certificates')
    def certificates_linkages(self) -> CertificatesLinkagesOfProfileEndpoint:
        return CertificatesLinkagesOfProfileEndpoint(self.id, self.session)
        
    @endpoint('/v1/profiles/{id}/relationships/devices')
    def devices_linkages(self) -> DevicesLinkagesOfProfileEndpoint:
        return DevicesLinkagesOfProfileEndpoint(self.id, self.session)
        
    def fields(self, *, profile: Union[ProfileField, list[ProfileField]]=None, bundle_id: Union[BundleIdField, list[BundleIdField]]=None, device: Union[DeviceField, list[DeviceField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None) -> ProfileEndpoint:
        '''Fields to return for included related types.

        :param profile: the fields to include for returned resources of type profiles
        :type profile: Union[ProfileField, list[ProfileField]] = None

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.ProfileEndpoint
        '''
        if profile: self._set_fields('profiles',profile if type(profile) is list else [profile])
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        if device: self._set_fields('devices',device if type(device) is list else [device])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    class Include(StringEnum):
        BUNDLE_ID = 'bundleId'
        DEVICES = 'devices'
        CERTIFICATES = 'certificates'

    def include(self, relationship: Union[Include, list[Include]]) -> ProfileEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ProfileEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, certificates: int=None, devices: int=None) -> ProfileEndpoint:
        '''Number of included related resources to return.

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :param devices: maximum number of related devices returned (when they are included). The maximum limit is 50
        :type devices: int = None

        :returns: self
        :rtype: applaud.endpoints.ProfileEndpoint
        '''
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit of certificates is 50')
        if certificates: self._set_limit(certificates, 'certificates')

        if devices and devices > 50:
            raise ValueError(f'The maximum limit of devices is 50')
        if devices: self._set_limit(devices, 'devices')

        return self

    def get(self) -> ProfileResponse:
        '''Get the resource.

        :returns: Single Profile
        :rtype: ProfileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfileResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class BundleIdLinkageOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/relationships/bundleId'

    def get(self) -> ProfileBundleIdLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: ProfileBundleIdLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfileBundleIdLinkageResponse.parse_obj(json)

class BundleIdOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/bundleId'

    def fields(self, *, bundle_id: Union[BundleIdField, list[BundleIdField]]=None) -> BundleIdOfProfileEndpoint:
        '''Fields to return for included related types.

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdOfProfileEndpoint
        '''
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        return self
        
    def get(self) -> BundleIdWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single BundleId with get
        :rtype: BundleIdWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BundleIdWithoutIncludesResponse.parse_obj(json)

class CertificatesLinkagesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/relationships/certificates'

    def limit(self, number: int=None) -> CertificatesLinkagesOfProfileEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesLinkagesOfProfileEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ProfileCertificatesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: ProfileCertificatesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfileCertificatesLinkagesResponse.parse_obj(json)

class CertificatesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/certificates'

    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None) -> CertificatesOfProfileEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfProfileEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    def limit(self, number: int=None) -> CertificatesOfProfileEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfProfileEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CertificatesWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of Certificates with get
        :rtype: CertificatesWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CertificatesWithoutIncludesResponse.parse_obj(json)

class DevicesLinkagesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/relationships/devices'

    def limit(self, number: int=None) -> DevicesLinkagesOfProfileEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DevicesLinkagesOfProfileEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ProfileDevicesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: ProfileDevicesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfileDevicesLinkagesResponse.parse_obj(json)

class DevicesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/devices'

    def fields(self, *, device: Union[DeviceField, list[DeviceField]]=None) -> DevicesOfProfileEndpoint:
        '''Fields to return for included related types.

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :returns: self
        :rtype: applaud.endpoints.DevicesOfProfileEndpoint
        '''
        if device: self._set_fields('devices',device if type(device) is list else [device])
        return self
        
    def limit(self, number: int=None) -> DevicesOfProfileEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DevicesOfProfileEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> DevicesWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of Devices with get
        :rtype: DevicesWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return DevicesWithoutIncludesResponse.parse_obj(json)

