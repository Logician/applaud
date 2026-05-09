from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AnalyticsReportRequestsEndpoint(Endpoint):
    path = '/v1/analyticsReportRequests'

    def create(self, request: AnalyticsReportRequestCreateRequest) -> AnalyticsReportRequestResponse:
        '''Create the resource.

        :param request: AnalyticsReportRequest representation
        :type request: AnalyticsReportRequestCreateRequest

        :returns: Single AnalyticsReportRequest
        :rtype: AnalyticsReportRequestResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AnalyticsReportRequestResponse.parse_obj(json)

class AnalyticsReportRequestEndpoint(IDEndpoint):
    path = '/v1/analyticsReportRequests/{id}'

    @endpoint('/v1/analyticsReportRequests/{id}/reports')
    def reports(self) -> ReportsOfAnalyticsReportRequestEndpoint:
        return ReportsOfAnalyticsReportRequestEndpoint(self.id, self.session)
        
    @endpoint('/v1/analyticsReportRequests/{id}/relationships/reports')
    def reports_linkages(self) -> ReportsLinkagesOfAnalyticsReportRequestEndpoint:
        return ReportsLinkagesOfAnalyticsReportRequestEndpoint(self.id, self.session)
        
    def fields(self, *, analytics_report_request: Union[AnalyticsReportRequestField, list[AnalyticsReportRequestField]]=None, analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]]=None) -> AnalyticsReportRequestEndpoint:
        '''Fields to return for included related types.

        :param analytics_report_request: the fields to include for returned resources of type analyticsReportRequests
        :type analytics_report_request: Union[AnalyticsReportRequestField, list[AnalyticsReportRequestField]] = None

        :param analytics_report: the fields to include for returned resources of type analyticsReports
        :type analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]] = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestEndpoint
        '''
        if analytics_report_request: self._set_fields('analyticsReportRequests',analytics_report_request if type(analytics_report_request) is list else [analytics_report_request])
        if analytics_report: self._set_fields('analyticsReports',analytics_report if type(analytics_report) is list else [analytics_report])
        return self
        
    class Include(StringEnum):
        REPORTS = 'reports'

    def include(self, relationship: Union[Include, list[Include]]) -> AnalyticsReportRequestEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, reports: int=None) -> AnalyticsReportRequestEndpoint:
        '''Number of included related resources to return.

        :param reports: maximum number of related reports returned (when they are included). The maximum limit is 50
        :type reports: int = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestEndpoint
        '''
        if reports and reports > 50:
            raise ValueError(f'The maximum limit of reports is 50')
        if reports: self._set_limit(reports, 'reports')

        return self

    def get(self) -> AnalyticsReportRequestResponse:
        '''Get the resource.

        :returns: Single AnalyticsReportRequest
        :rtype: AnalyticsReportRequestResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportRequestResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class ReportsLinkagesOfAnalyticsReportRequestEndpoint(IDEndpoint):
    path = '/v1/analyticsReportRequests/{id}/relationships/reports'

    def limit(self, number: int=None) -> ReportsLinkagesOfAnalyticsReportRequestEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReportsLinkagesOfAnalyticsReportRequestEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AnalyticsReportRequestReportsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AnalyticsReportRequestReportsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportRequestReportsLinkagesResponse.parse_obj(json)

class ReportsOfAnalyticsReportRequestEndpoint(IDEndpoint):
    path = '/v1/analyticsReportRequests/{id}/reports'

    class Category(StringEnum):
        APP_USAGE = 'APP_USAGE'
        APP_STORE_ENGAGEMENT = 'APP_STORE_ENGAGEMENT'
        COMMERCE = 'COMMERCE'
        FRAMEWORK_USAGE = 'FRAMEWORK_USAGE'
        PERFORMANCE = 'PERFORMANCE'

    def fields(self, *, analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]]=None) -> ReportsOfAnalyticsReportRequestEndpoint:
        '''Fields to return for included related types.

        :param analytics_report: the fields to include for returned resources of type analyticsReports
        :type analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReportsOfAnalyticsReportRequestEndpoint
        '''
        if analytics_report: self._set_fields('analyticsReports',analytics_report if type(analytics_report) is list else [analytics_report])
        return self
        
    def filter(self, *, name: Union[str, list[str]]=None, category: Union[Category, list[Category]]=None) -> ReportsOfAnalyticsReportRequestEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param category: filter by attribute 'category'
        :type category: Union[Category, list[Category]] = None

        :returns: self
        :rtype: applaud.endpoints.ReportsOfAnalyticsReportRequestEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if category: self._set_filter('category', category if type(category) is list else [category])
        
        return self
        
    def limit(self, number: int=None) -> ReportsOfAnalyticsReportRequestEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReportsOfAnalyticsReportRequestEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AnalyticsReportsResponse:
        '''Get one or more resources.

        :returns: List of AnalyticsReports
        :rtype: AnalyticsReportsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportsResponse.parse_obj(json)

