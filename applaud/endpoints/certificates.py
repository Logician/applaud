from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CertificatesEndpoint(Endpoint):
    path = '/v1/certificates'

    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None, pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]]=None) -> CertificatesEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :param pass_type_id: the fields to include for returned resources of type passTypeIds
        :type pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        if pass_type_id: self._set_fields('passTypeIds',pass_type_id if type(pass_type_id) is list else [pass_type_id])
        return self
        
    class Include(StringEnum):
        PASS_TYPE_ID = 'passTypeId'

    def filter(self, *, display_name: Union[str, list[str]]=None, certificate_type: Union[CertificateType, list[CertificateType]]=None, serial_number: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> CertificatesEndpoint:
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
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if display_name: self._set_filter('displayName', display_name if type(display_name) is list else [display_name])
        
        if certificate_type: self._set_filter('certificateType', certificate_type if type(certificate_type) is list else [certificate_type])
        
        if serial_number: self._set_filter('serialNumber', serial_number if type(serial_number) is list else [serial_number])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CertificatesEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, display_name: SortOrder=None, certificate_type: SortOrder=None, serial_number: SortOrder=None, id: SortOrder=None) -> CertificatesEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if display_name: self.sort_expressions.append('displayName' if display_name == SortOrder.ASC else '-displayName')
        if certificate_type: self.sort_expressions.append('certificateType' if certificate_type == SortOrder.ASC else '-certificateType')
        if serial_number: self.sort_expressions.append('serialNumber' if serial_number == SortOrder.ASC else '-serialNumber')
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        return self
        
    def limit(self, number: int=None) -> CertificatesEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
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

    def create(self, request: CertificateCreateRequest) -> CertificateResponse:
        '''Create the resource.

        :param request: Certificate representation
        :type request: CertificateCreateRequest

        :returns: Single Certificate
        :rtype: CertificateResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return CertificateResponse.parse_obj(json)

class CertificateEndpoint(IDEndpoint):
    path = '/v1/certificates/{id}'

    @endpoint('/v1/certificates/{id}/passTypeId')
    def pass_type_id(self) -> PassTypeIdOfCertificateEndpoint:
        return PassTypeIdOfCertificateEndpoint(self.id, self.session)
        
    @endpoint('/v1/certificates/{id}/relationships/passTypeId')
    def pass_type_id_linkage(self) -> PassTypeIdLinkageOfCertificateEndpoint:
        return PassTypeIdLinkageOfCertificateEndpoint(self.id, self.session)
        
    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None, pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]]=None) -> CertificateEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :param pass_type_id: the fields to include for returned resources of type passTypeIds
        :type pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificateEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        if pass_type_id: self._set_fields('passTypeIds',pass_type_id if type(pass_type_id) is list else [pass_type_id])
        return self
        
    class Include(StringEnum):
        PASS_TYPE_ID = 'passTypeId'

    def include(self, relationship: Union[Include, list[Include]]) -> CertificateEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CertificateEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> CertificateResponse:
        '''Get the resource.

        :returns: Single Certificate
        :rtype: CertificateResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CertificateResponse.parse_obj(json)

    def update(self, request: CertificateUpdateRequest) -> CertificateResponse:
        '''Modify the resource.

        :param request: Certificate representation
        :type request: CertificateUpdateRequest

        :returns: Single Certificate
        :rtype: CertificateResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return CertificateResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class PassTypeIdLinkageOfCertificateEndpoint(IDEndpoint):
    path = '/v1/certificates/{id}/relationships/passTypeId'

    def get(self) -> CertificatePassTypeIdLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: CertificatePassTypeIdLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CertificatePassTypeIdLinkageResponse.parse_obj(json)

class PassTypeIdOfCertificateEndpoint(IDEndpoint):
    path = '/v1/certificates/{id}/passTypeId'

    def fields(self, *, pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None) -> PassTypeIdOfCertificateEndpoint:
        '''Fields to return for included related types.

        :param pass_type_id: the fields to include for returned resources of type passTypeIds
        :type pass_type_id: Union[PassTypeIdField, list[PassTypeIdField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdOfCertificateEndpoint
        '''
        if pass_type_id: self._set_fields('passTypeIds',pass_type_id if type(pass_type_id) is list else [pass_type_id])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    class Include(StringEnum):
        CERTIFICATES = 'certificates'

    def include(self, relationship: Union[Include, list[Include]]) -> PassTypeIdOfCertificateEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdOfCertificateEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, certificates: int=None) -> PassTypeIdOfCertificateEndpoint:
        '''Number of included related resources to return.

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :returns: self
        :rtype: applaud.endpoints.PassTypeIdOfCertificateEndpoint
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

