from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class PassTypeIdsEndpoint(Endpoint):
    path = '/v1/passTypeIds'

    def fields(self, *, pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None) -> PassTypeIdsEndpoint:
        '''Fields to return for included related types.

        :param pass_type_id: the fields to include for returned resources of type passTypeIds
        :type pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdsEndpoint
        '''
        if pass_type_id: self._set_fields('passTypeIds',pass_type_id if type(pass_type_id) is list else [pass_type_id])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    class Include(StringEnum):
        CERTIFICATES = 'certificates'

    def filter(self, *, name: Union[str, list[str]]=None, identifier: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> PassTypeIdsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param identifier: filter by attribute 'identifier'
        :type identifier: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdsEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if identifier: self._set_filter('identifier', identifier if type(identifier) is list else [identifier])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PassTypeIdsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None, identifier: SortOrder=None, id: SortOrder=None) -> PassTypeIdsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdsEndpoint
        '''
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if identifier: self.sort_expressions.append('identifier' if identifier == SortOrder.ASC else '-identifier')
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        return self
        
    def limit(self, number: int=None, *, certificates: int=None) -> PassTypeIdsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit of certificates is 50')
        if certificates: self._set_limit(certificates, 'certificates')

        return self

    def get(self) -> PassTypeIdsResponse:
        '''Get one or more resources.

        :returns: List of PassTypeIds
        :rtype: PassTypeIdsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PassTypeIdsResponse.parse_obj(json)

    def create(self, request: PassTypeIdCreateRequest) -> PassTypeIdResponse:
        '''Create the resource.

        :param request: PassTypeId representation
        :type request: PassTypeIdCreateRequest

        :returns: Single PassTypeId
        :rtype: PassTypeIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return PassTypeIdResponse.parse_obj(json)

class PassTypeIdEndpoint(IDEndpoint):
    path = '/v1/passTypeIds/{id}'

    @endpoint('/v1/passTypeIds/{id}/certificates')
    def certificates(self) -> CertificatesOfPassTypeIdEndpoint:
        return CertificatesOfPassTypeIdEndpoint(self.id, self.session)
        
    @endpoint('/v1/passTypeIds/{id}/relationships/certificates')
    def certificates_linkages(self) -> CertificatesLinkagesOfPassTypeIdEndpoint:
        return CertificatesLinkagesOfPassTypeIdEndpoint(self.id, self.session)
        
    def fields(self, *, pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None) -> PassTypeIdEndpoint:
        '''Fields to return for included related types.

        :param pass_type_id: the fields to include for returned resources of type passTypeIds
        :type pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdEndpoint
        '''
        if pass_type_id: self._set_fields('passTypeIds',pass_type_id if type(pass_type_id) is list else [pass_type_id])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    class Include(StringEnum):
        CERTIFICATES = 'certificates'

    def include(self, relationship: Union[Include, list[Include]]) -> PassTypeIdEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, certificates: int=None) -> PassTypeIdEndpoint:
        '''Number of included related resources to return.

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdEndpoint
        '''
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit of certificates is 50')
        if certificates: self._set_limit(certificates, 'certificates')

        return self

    def get(self) -> PassTypeIdResponse:
        '''Get the resource.

        :returns: Single PassTypeId
        :rtype: PassTypeIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PassTypeIdResponse.parse_obj(json)

    def update(self, request: PassTypeIdUpdateRequest) -> PassTypeIdResponse:
        '''Modify the resource.

        :param request: PassTypeId representation
        :type request: PassTypeIdUpdateRequest

        :returns: Single PassTypeId
        :rtype: PassTypeIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return PassTypeIdResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class CertificatesLinkagesOfPassTypeIdEndpoint(IDEndpoint):
    path = '/v1/passTypeIds/{id}/relationships/certificates'

    def limit(self, number: int=None) -> CertificatesLinkagesOfPassTypeIdEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesLinkagesOfPassTypeIdEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> PassTypeIdCertificatesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: PassTypeIdCertificatesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PassTypeIdCertificatesLinkagesResponse.parse_obj(json)

class CertificatesOfPassTypeIdEndpoint(IDEndpoint):
    path = '/v1/passTypeIds/{id}/certificates'

    class CertificateType(StringEnum):
        APPLE_PAY = 'APPLE_PAY'
        APPLE_PAY_MERCHANT_IDENTITY = 'APPLE_PAY_MERCHANT_IDENTITY'
        APPLE_PAY_PSP_IDENTITY = 'APPLE_PAY_PSP_IDENTITY'
        APPLE_PAY_RSA = 'APPLE_PAY_RSA'
        DEVELOPER_ID_KEXT = 'DEVELOPER_ID_KEXT'
        DEVELOPER_ID_KEXT_G2 = 'DEVELOPER_ID_KEXT_G2'
        DEVELOPER_ID_APPLICATION = 'DEVELOPER_ID_APPLICATION'
        DEVELOPER_ID_APPLICATION_G2 = 'DEVELOPER_ID_APPLICATION_G2'
        DEVELOPMENT = 'DEVELOPMENT'
        DISTRIBUTION = 'DISTRIBUTION'
        IDENTITY_ACCESS = 'IDENTITY_ACCESS'
        IOS_DEVELOPMENT = 'IOS_DEVELOPMENT'
        IOS_DISTRIBUTION = 'IOS_DISTRIBUTION'
        MAC_APP_DISTRIBUTION = 'MAC_APP_DISTRIBUTION'
        MAC_INSTALLER_DISTRIBUTION = 'MAC_INSTALLER_DISTRIBUTION'
        MAC_APP_DEVELOPMENT = 'MAC_APP_DEVELOPMENT'
        PASS_TYPE_ID = 'PASS_TYPE_ID'
        PASS_TYPE_ID_WITH_NFC = 'PASS_TYPE_ID_WITH_NFC'

    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None, pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]]=None) -> CertificatesOfPassTypeIdEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :param pass_type_id: the fields to include for returned resources of type passTypeIds
        :type pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfPassTypeIdEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        if pass_type_id: self._set_fields('passTypeIds',pass_type_id if type(pass_type_id) is list else [pass_type_id])
        return self
        
    class Include(StringEnum):
        PASS_TYPE_ID = 'passTypeId'

    def filter(self, *, display_name: Union[str, list[str]]=None, certificate_type: Union[CertificateType, list[CertificateType]]=None, serial_number: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> CertificatesOfPassTypeIdEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param display_name: filter by attribute 'displayName'
        :type display_name: Union[str, list[str]] = None

        :param certificate_type: filter by attribute 'certificateType'
        :type certificate_type: Union[CertificateType, list[CertificateType]] = None

        :param serial_number: filter by attribute 'serialNumber'
        :type serial_number: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfPassTypeIdEndpoint
        '''
        if display_name: self._set_filter('displayName', display_name if type(display_name) is list else [display_name])
        
        if certificate_type: self._set_filter('certificateType', certificate_type if type(certificate_type) is list else [certificate_type])
        
        if serial_number: self._set_filter('serialNumber', serial_number if type(serial_number) is list else [serial_number])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CertificatesOfPassTypeIdEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfPassTypeIdEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, display_name: SortOrder=None, certificate_type: SortOrder=None, serial_number: SortOrder=None, id: SortOrder=None) -> CertificatesOfPassTypeIdEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfPassTypeIdEndpoint
        '''
        if display_name: self.sort_expressions.append('displayName' if display_name == SortOrder.ASC else '-displayName')
        if certificate_type: self.sort_expressions.append('certificateType' if certificate_type == SortOrder.ASC else '-certificateType')
        if serial_number: self.sort_expressions.append('serialNumber' if serial_number == SortOrder.ASC else '-serialNumber')
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        return self
        
    def limit(self, number: int=None) -> CertificatesOfPassTypeIdEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfPassTypeIdEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CertificatesResponse:
        '''Get one or more resources.

        :returns: List of Certificates
        :rtype: CertificatesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CertificatesResponse.parse_obj(json)

