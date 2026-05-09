from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseContentEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseContents/{id}'

    def fields(self, *, in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]]=None) -> InAppPurchaseContentEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_content: the fields to include for returned resources of type inAppPurchaseContents
        :type in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseContentEndpoint
        '''
        if in_app_purchase_content: self._set_fields('inAppPurchaseContents',in_app_purchase_content if type(in_app_purchase_content) is list else [in_app_purchase_content])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseContentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseContentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseContentResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseContent
        :rtype: InAppPurchaseContentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseContentResponse.parse_obj(json)

