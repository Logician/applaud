from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AccessibilityDeclarationsEndpoint(Endpoint):
    path = '/v1/accessibilityDeclarations'

    def create(self, request: AccessibilityDeclarationCreateRequest) -> AccessibilityDeclarationResponse:
        '''Create the resource.

        :param request: AccessibilityDeclaration representation
        :type request: AccessibilityDeclarationCreateRequest

        :returns: Single AccessibilityDeclaration
        :rtype: AccessibilityDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AccessibilityDeclarationResponse.parse_obj(json)

class AccessibilityDeclarationEndpoint(IDEndpoint):
    path = '/v1/accessibilityDeclarations/{id}'

    def fields(self, *, accessibility_declaration: Union[AccessibilityDeclarationField, list[AccessibilityDeclarationField]]=None) -> AccessibilityDeclarationEndpoint:
        '''Fields to return for included related types.

        :param accessibility_declaration: the fields to include for returned resources of type accessibilityDeclarations
        :type accessibility_declaration: Union[AccessibilityDeclarationField, list[AccessibilityDeclarationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AccessibilityDeclarationEndpoint
        '''
        if accessibility_declaration: self._set_fields('accessibilityDeclarations',accessibility_declaration if type(accessibility_declaration) is list else [accessibility_declaration])
        return self
        
    def get(self) -> AccessibilityDeclarationResponse:
        '''Get the resource.

        :returns: Single AccessibilityDeclaration
        :rtype: AccessibilityDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AccessibilityDeclarationResponse.parse_obj(json)

    def update(self, request: AccessibilityDeclarationUpdateRequest) -> AccessibilityDeclarationResponse:
        '''Modify the resource.

        :param request: AccessibilityDeclaration representation
        :type request: AccessibilityDeclarationUpdateRequest

        :returns: Single AccessibilityDeclaration
        :rtype: AccessibilityDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AccessibilityDeclarationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

