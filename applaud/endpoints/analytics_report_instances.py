from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AnalyticsReportInstanceEndpoint(IDEndpoint):
    path = '/v1/analyticsReportInstances/{id}'

    @endpoint('/v1/analyticsReportInstances/{id}/segments')
    def segments(self) -> SegmentsOfAnalyticsReportInstanceEndpoint:
        return SegmentsOfAnalyticsReportInstanceEndpoint(self.id, self.session)
        
    @endpoint('/v1/analyticsReportInstances/{id}/relationships/segments')
    def segments_linkages(self) -> SegmentsLinkagesOfAnalyticsReportInstanceEndpoint:
        return SegmentsLinkagesOfAnalyticsReportInstanceEndpoint(self.id, self.session)
        
    def fields(self, *, analytics_report_instance: Union[AnalyticsReportInstanceField, list[AnalyticsReportInstanceField]]=None) -> AnalyticsReportInstanceEndpoint:
        '''Fields to return for included related types.

        :param analytics_report_instance: the fields to include for returned resources of type analyticsReportInstances
        :type analytics_report_instance: Union[AnalyticsReportInstanceField, list[AnalyticsReportInstanceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportInstanceEndpoint
        '''
        if analytics_report_instance: self._set_fields('analyticsReportInstances',analytics_report_instance if type(analytics_report_instance) is list else [analytics_report_instance])
        return self
        
    def get(self) -> AnalyticsReportInstanceResponse:
        '''Get the resource.

        :returns: Single AnalyticsReportInstance
        :rtype: AnalyticsReportInstanceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportInstanceResponse.parse_obj(json)

class SegmentsLinkagesOfAnalyticsReportInstanceEndpoint(IDEndpoint):
    path = '/v1/analyticsReportInstances/{id}/relationships/segments'

    def limit(self, number: int=None) -> SegmentsLinkagesOfAnalyticsReportInstanceEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SegmentsLinkagesOfAnalyticsReportInstanceEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AnalyticsReportInstanceSegmentsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AnalyticsReportInstanceSegmentsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportInstanceSegmentsLinkagesResponse.parse_obj(json)

class SegmentsOfAnalyticsReportInstanceEndpoint(IDEndpoint):
    path = '/v1/analyticsReportInstances/{id}/segments'

    def fields(self, *, analytics_report_segment: Union[AnalyticsReportSegmentField, list[AnalyticsReportSegmentField]]=None) -> SegmentsOfAnalyticsReportInstanceEndpoint:
        '''Fields to return for included related types.

        :param analytics_report_segment: the fields to include for returned resources of type analyticsReportSegments
        :type analytics_report_segment: Union[AnalyticsReportSegmentField, list[AnalyticsReportSegmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.SegmentsOfAnalyticsReportInstanceEndpoint
        '''
        if analytics_report_segment: self._set_fields('analyticsReportSegments',analytics_report_segment if type(analytics_report_segment) is list else [analytics_report_segment])
        return self
        
    def limit(self, number: int=None) -> SegmentsOfAnalyticsReportInstanceEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SegmentsOfAnalyticsReportInstanceEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AnalyticsReportSegmentsResponse:
        '''Get one or more resources.

        :returns: List of AnalyticsReportSegments
        :rtype: AnalyticsReportSegmentsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportSegmentsResponse.parse_obj(json)

