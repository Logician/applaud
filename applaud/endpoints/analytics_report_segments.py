from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AnalyticsReportSegmentEndpoint(IDEndpoint):
    path = '/v1/analyticsReportSegments/{id}'

    def fields(self, *, analytics_report_segment: Union[AnalyticsReportSegmentField, list[AnalyticsReportSegmentField]]=None) -> AnalyticsReportSegmentEndpoint:
        '''Fields to return for included related types.

        :param analytics_report_segment: the fields to include for returned resources of type analyticsReportSegments
        :type analytics_report_segment: Union[AnalyticsReportSegmentField, list[AnalyticsReportSegmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportSegmentEndpoint
        '''
        if analytics_report_segment: self._set_fields('analyticsReportSegments',analytics_report_segment if type(analytics_report_segment) is list else [analytics_report_segment])
        return self
        
    def get(self) -> AnalyticsReportSegmentResponse:
        '''Get the resource.

        :returns: Single AnalyticsReportSegment
        :rtype: AnalyticsReportSegmentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportSegmentResponse.parse_obj(json)

