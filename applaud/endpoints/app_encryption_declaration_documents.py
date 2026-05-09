from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppEncryptionDeclarationDocumentsEndpoint(Endpoint):
    path = '/v1/appEncryptionDeclarationDocuments'

    def create(self, request: AppEncryptionDeclarationDocumentCreateRequest) -> AppEncryptionDeclarationDocumentResponse:
        '''Create the resource.

        :param request: AppEncryptionDeclarationDocument representation
        :type request: AppEncryptionDeclarationDocumentCreateRequest

        :returns: Single AppEncryptionDeclarationDocument
        :rtype: AppEncryptionDeclarationDocumentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppEncryptionDeclarationDocumentResponse.parse_obj(json)

class AppEncryptionDeclarationDocumentEndpoint(IDEndpoint):
    path = '/v1/appEncryptionDeclarationDocuments/{id}'

    def fields(self, *, app_encryption_declaration_document: Union[AppEncryptionDeclarationDocumentField, list[AppEncryptionDeclarationDocumentField]]=None) -> AppEncryptionDeclarationDocumentEndpoint:
        '''Fields to return for included related types.

        :param app_encryption_declaration_document: the fields to include for returned resources of type appEncryptionDeclarationDocuments
        :type app_encryption_declaration_document: Union[AppEncryptionDeclarationDocumentField, list[AppEncryptionDeclarationDocumentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationDocumentEndpoint
        '''
        if app_encryption_declaration_document: self._set_fields('appEncryptionDeclarationDocuments',app_encryption_declaration_document if type(app_encryption_declaration_document) is list else [app_encryption_declaration_document])
        return self
        
    def get(self) -> AppEncryptionDeclarationDocumentResponse:
        '''Get the resource.

        :returns: Single AppEncryptionDeclarationDocument
        :rtype: AppEncryptionDeclarationDocumentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEncryptionDeclarationDocumentResponse.parse_obj(json)

    def update(self, request: AppEncryptionDeclarationDocumentUpdateRequest) -> AppEncryptionDeclarationDocumentResponse:
        '''Modify the resource.

        :param request: AppEncryptionDeclarationDocument representation
        :type request: AppEncryptionDeclarationDocumentUpdateRequest

        :returns: Single AppEncryptionDeclarationDocument
        :rtype: AppEncryptionDeclarationDocumentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppEncryptionDeclarationDocumentResponse.parse_obj(json)

