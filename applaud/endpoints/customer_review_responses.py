from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CustomerReviewResponsesEndpoint(Endpoint):
    path = '/v1/customerReviewResponses'

    def create(self, request: CustomerReviewResponseV1CreateRequest) -> CustomerReviewResponseV1Response:
        '''Create the resource.

        :param request: CustomerReviewResponse representation
        :type request: CustomerReviewResponseV1CreateRequest

        :returns: Single CustomerReviewResponse
        :rtype: CustomerReviewResponseV1Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return CustomerReviewResponseV1Response.parse_obj(json)

class CustomerReviewResponseEndpoint(IDEndpoint):
    path = '/v1/customerReviewResponses/{id}'

    def fields(self, *, customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]]=None) -> CustomerReviewResponseEndpoint:
        '''Fields to return for included related types.

        :param customer_review_response: the fields to include for returned resources of type customerReviewResponses
        :type customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewResponseEndpoint
        '''
        if customer_review_response: self._set_fields('customerReviewResponses',customer_review_response if type(customer_review_response) is list else [customer_review_response])
        return self
        
    class Include(StringEnum):
        REVIEW = 'review'

    def include(self, relationship: Union[Include, list[Include]]) -> CustomerReviewResponseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewResponseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> CustomerReviewResponseV1Response:
        '''Get the resource.

        :returns: Single CustomerReviewResponse
        :rtype: CustomerReviewResponseV1Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CustomerReviewResponseV1Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

