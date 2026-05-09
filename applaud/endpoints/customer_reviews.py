from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CustomerReviewEndpoint(IDEndpoint):
    path = '/v1/customerReviews/{id}'

    @endpoint('/v1/customerReviews/{id}/response')
    def response(self) -> ResponseOfCustomerReviewEndpoint:
        return ResponseOfCustomerReviewEndpoint(self.id, self.session)
        
    @endpoint('/v1/customerReviews/{id}/relationships/response')
    def response_linkage(self) -> ResponseLinkageOfCustomerReviewEndpoint:
        return ResponseLinkageOfCustomerReviewEndpoint(self.id, self.session)
        
    def fields(self, *, customer_review: Union[CustomerReviewField, list[CustomerReviewField]]=None, customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]]=None) -> CustomerReviewEndpoint:
        '''Fields to return for included related types.

        :param customer_review: the fields to include for returned resources of type customerReviews
        :type customer_review: Union[CustomerReviewField, list[CustomerReviewField]] = None

        :param customer_review_response: the fields to include for returned resources of type customerReviewResponses
        :type customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewEndpoint
        '''
        if customer_review: self._set_fields('customerReviews',customer_review if type(customer_review) is list else [customer_review])
        if customer_review_response: self._set_fields('customerReviewResponses',customer_review_response if type(customer_review_response) is list else [customer_review_response])
        return self
        
    class Include(StringEnum):
        RESPONSE = 'response'

    def include(self, relationship: Union[Include, list[Include]]) -> CustomerReviewEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> CustomerReviewResponse:
        '''Get the resource.

        :returns: Single CustomerReview
        :rtype: CustomerReviewResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CustomerReviewResponse.parse_obj(json)

class ResponseLinkageOfCustomerReviewEndpoint(IDEndpoint):
    path = '/v1/customerReviews/{id}/relationships/response'

    def get(self) -> CustomerReviewResponseLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: CustomerReviewResponseLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CustomerReviewResponseLinkageResponse.parse_obj(json)

class ResponseOfCustomerReviewEndpoint(IDEndpoint):
    path = '/v1/customerReviews/{id}/response'

    def fields(self, *, customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]]=None, customer_review: Union[CustomerReviewField, list[CustomerReviewField]]=None) -> ResponseOfCustomerReviewEndpoint:
        '''Fields to return for included related types.

        :param customer_review_response: the fields to include for returned resources of type customerReviewResponses
        :type customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]] = None

        :param customer_review: the fields to include for returned resources of type customerReviews
        :type customer_review: Union[CustomerReviewField, list[CustomerReviewField]] = None

        :returns: self
        :rtype: applaud.endpoints.ResponseOfCustomerReviewEndpoint
        '''
        if customer_review_response: self._set_fields('customerReviewResponses',customer_review_response if type(customer_review_response) is list else [customer_review_response])
        if customer_review: self._set_fields('customerReviews',customer_review if type(customer_review) is list else [customer_review])
        return self
        
    class Include(StringEnum):
        REVIEW = 'review'

    def include(self, relationship: Union[Include, list[Include]]) -> ResponseOfCustomerReviewEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ResponseOfCustomerReviewEndpoint
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

