from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class MerchantIdsEndpoint(Endpoint):
    path = '/v1/merchantIds'

    def fields(self, *, merchant_id: Union[MerchantIdField, list[MerchantIdField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None) -> MerchantIdsEndpoint:
        '''Fields to return for included related types.

        :param merchant_id: the fields to include for returned resources of type merchantIds
        :type merchant_id: Union[MerchantIdField, list[MerchantIdField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.MerchantIdsEndpoint
        '''
        if merchant_id: self._set_fields('merchantIds',merchant_id if type(merchant_id) is list else [merchant_id])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    class Include(StringEnum):
        CERTIFICATES = 'certificates'

    def filter(self, *, name: Union[str, list[str]]=None, identifier: Union[str, list[str]]=None) -> MerchantIdsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param identifier: filter by attribute 'identifier'
        :type identifier: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.MerchantIdsEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if identifier: self._set_filter('identifier', identifier if type(identifier) is list else [identifier])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> MerchantIdsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.MerchantIdsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None, identifier: SortOrder=None) -> MerchantIdsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.MerchantIdsEndpoint
        '''
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if identifier: self.sort_expressions.append('identifier' if identifier == SortOrder.ASC else '-identifier')
        return self
        
    def limit(self, number: int=None, *, certificates: int=None) -> MerchantIdsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :returns: self
        :rtype: applaud.endpoints.MerchantIdsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit of certificates is 50')
        if certificates: self._set_limit(certificates, 'certificates')

        return self

    def get(self) -> MerchantIdsResponse:
        '''Get one or more resources.

        :returns: List of MerchantIds
        :rtype: MerchantIdsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return MerchantIdsResponse.parse_obj(json)

    def create(self, request: MerchantIdCreateRequest) -> MerchantIdResponse:
        '''Create the resource.

        :param request: MerchantId representation
        :type request: MerchantIdCreateRequest

        :returns: Single MerchantId
        :rtype: MerchantIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return MerchantIdResponse.parse_obj(json)

class MerchantIdEndpoint(IDEndpoint):
    path = '/v1/merchantIds/{id}'

    @endpoint('/v1/merchantIds/{id}/certificates')
    def certificates(self) -> CertificatesOfMerchantIdEndpoint:
        return CertificatesOfMerchantIdEndpoint(self.id, self.session)
        
    @endpoint('/v1/merchantIds/{id}/relationships/certificates')
    def certificates_linkages(self) -> CertificatesLinkagesOfMerchantIdEndpoint:
        return CertificatesLinkagesOfMerchantIdEndpoint(self.id, self.session)
        
    def fields(self, *, merchant_id: Union[MerchantIdField, list[MerchantIdField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None) -> MerchantIdEndpoint:
        '''Fields to return for included related types.

        :param merchant_id: the fields to include for returned resources of type merchantIds
        :type merchant_id: Union[MerchantIdField, list[MerchantIdField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.MerchantIdEndpoint
        '''
        if merchant_id: self._set_fields('merchantIds',merchant_id if type(merchant_id) is list else [merchant_id])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    class Include(StringEnum):
        CERTIFICATES = 'certificates'

    def include(self, relationship: Union[Include, list[Include]]) -> MerchantIdEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.MerchantIdEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, certificates: int=None) -> MerchantIdEndpoint:
        '''Number of included related resources to return.

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :returns: self
        :rtype: applaud.endpoints.MerchantIdEndpoint
        '''
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit of certificates is 50')
        if certificates: self._set_limit(certificates, 'certificates')

        return self

    def get(self) -> MerchantIdResponse:
        '''Get the resource.

        :returns: Single MerchantId
        :rtype: MerchantIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return MerchantIdResponse.parse_obj(json)

    def update(self, request: MerchantIdUpdateRequest) -> MerchantIdResponse:
        '''Modify the resource.

        :param request: MerchantId representation
        :type request: MerchantIdUpdateRequest

        :returns: Single MerchantId
        :rtype: MerchantIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return MerchantIdResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class CertificatesLinkagesOfMerchantIdEndpoint(IDEndpoint):
    path = '/v1/merchantIds/{id}/relationships/certificates'

    def limit(self, number: int=None) -> CertificatesLinkagesOfMerchantIdEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesLinkagesOfMerchantIdEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> MerchantIdCertificatesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: MerchantIdCertificatesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return MerchantIdCertificatesLinkagesResponse.parse_obj(json)

class CertificatesOfMerchantIdEndpoint(IDEndpoint):
    path = '/v1/merchantIds/{id}/certificates'

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

    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None, pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]]=None) -> CertificatesOfMerchantIdEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :param pass_type_id: the fields to include for returned resources of type passTypeIds
        :type pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfMerchantIdEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        if pass_type_id: self._set_fields('passTypeIds',pass_type_id if type(pass_type_id) is list else [pass_type_id])
        return self
        
    class Include(StringEnum):
        PASS_TYPE_ID = 'passTypeId'

    def filter(self, *, display_name: Union[str, list[str]]=None, certificate_type: Union[CertificateType, list[CertificateType]]=None, serial_number: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> CertificatesOfMerchantIdEndpoint:
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
        :rtype: applaud.endpoints.CertificatesOfMerchantIdEndpoint
        '''
        if display_name: self._set_filter('displayName', display_name if type(display_name) is list else [display_name])
        
        if certificate_type: self._set_filter('certificateType', certificate_type if type(certificate_type) is list else [certificate_type])
        
        if serial_number: self._set_filter('serialNumber', serial_number if type(serial_number) is list else [serial_number])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CertificatesOfMerchantIdEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfMerchantIdEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, display_name: SortOrder=None, certificate_type: SortOrder=None, serial_number: SortOrder=None, id: SortOrder=None) -> CertificatesOfMerchantIdEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfMerchantIdEndpoint
        '''
        if display_name: self.sort_expressions.append('displayName' if display_name == SortOrder.ASC else '-displayName')
        if certificate_type: self.sort_expressions.append('certificateType' if certificate_type == SortOrder.ASC else '-certificateType')
        if serial_number: self.sort_expressions.append('serialNumber' if serial_number == SortOrder.ASC else '-serialNumber')
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        return self
        
    def limit(self, number: int=None) -> CertificatesOfMerchantIdEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfMerchantIdEndpoint
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

