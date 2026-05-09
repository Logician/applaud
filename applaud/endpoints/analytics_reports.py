from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AnalyticsReportEndpoint(IDEndpoint):
    path = '/v1/analyticsReports/{id}'

    @endpoint('/v1/analyticsReports/{id}/instances')
    def instances(self) -> InstancesOfAnalyticsReportEndpoint:
        return InstancesOfAnalyticsReportEndpoint(self.id, self.session)
        
    @endpoint('/v1/analyticsReports/{id}/relationships/instances')
    def instances_linkages(self) -> InstancesLinkagesOfAnalyticsReportEndpoint:
        return InstancesLinkagesOfAnalyticsReportEndpoint(self.id, self.session)
        
    def fields(self, *, analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]]=None) -> AnalyticsReportEndpoint:
        '''Fields to return for included related types.

        :param analytics_report: the fields to include for returned resources of type analyticsReports
        :type analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]] = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportEndpoint
        '''
        if analytics_report: self._set_fields('analyticsReports',analytics_report if type(analytics_report) is list else [analytics_report])
        return self
        
    def get(self) -> AnalyticsReportResponse:
        '''Get the resource.

        :returns: Single AnalyticsReport
        :rtype: AnalyticsReportResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportResponse.parse_obj(json)

class InstancesLinkagesOfAnalyticsReportEndpoint(IDEndpoint):
    path = '/v1/analyticsReports/{id}/relationships/instances'

    def limit(self, number: int=None) -> InstancesLinkagesOfAnalyticsReportEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.InstancesLinkagesOfAnalyticsReportEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AnalyticsReportInstancesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AnalyticsReportInstancesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportInstancesLinkagesResponse.parse_obj(json)

class InstancesOfAnalyticsReportEndpoint(IDEndpoint):
    path = '/v1/analyticsReports/{id}/instances'

    class Granularity(StringEnum):
        DAILY = 'DAILY'
        WEEKLY = 'WEEKLY'
        MONTHLY = 'MONTHLY'

    def fields(self, *, analytics_report_instance: Union[AnalyticsReportInstanceField, list[AnalyticsReportInstanceField]]=None) -> InstancesOfAnalyticsReportEndpoint:
        '''Fields to return for included related types.

        :param analytics_report_instance: the fields to include for returned resources of type analyticsReportInstances
        :type analytics_report_instance: Union[AnalyticsReportInstanceField, list[AnalyticsReportInstanceField]] = None

        :returns: self
        :rtype: applaud.endpoints.InstancesOfAnalyticsReportEndpoint
        '''
        if analytics_report_instance: self._set_fields('analyticsReportInstances',analytics_report_instance if type(analytics_report_instance) is list else [analytics_report_instance])
        return self
        
    def filter(self, *, granularity: Union[Granularity, list[Granularity]]=None, processing_date: Union[str, list[str]]=None) -> InstancesOfAnalyticsReportEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param granularity: filter by attribute 'granularity'
        :type granularity: Union[Granularity, list[Granularity]] = None

        :param processing_date: filter by attribute 'processingDate'
        :type processing_date: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.InstancesOfAnalyticsReportEndpoint
        '''
        if granularity: self._set_filter('granularity', granularity if type(granularity) is list else [granularity])
        
        if processing_date: self._set_filter('processingDate', processing_date if type(processing_date) is list else [processing_date])
        
        return self
        
    def limit(self, number: int=None) -> InstancesOfAnalyticsReportEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.InstancesOfAnalyticsReportEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AnalyticsReportInstancesResponse:
        '''Get one or more resources.

        :returns: List of AnalyticsReportInstances
        :rtype: AnalyticsReportInstancesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportInstancesResponse.parse_obj(json)

