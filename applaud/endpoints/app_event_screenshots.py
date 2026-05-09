from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppEventScreenshotsEndpoint(Endpoint):
    path = '/v1/appEventScreenshots'

    def create(self, request: AppEventScreenshotCreateRequest) -> AppEventScreenshotResponse:
        '''Create the resource.

        :param request: AppEventScreenshot representation
        :type request: AppEventScreenshotCreateRequest

        :returns: Single AppEventScreenshot
        :rtype: AppEventScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppEventScreenshotResponse.parse_obj(json)

class AppEventScreenshotEndpoint(IDEndpoint):
    path = '/v1/appEventScreenshots/{id}'

    def fields(self, *, app_event_screenshot: Union[AppEventScreenshotField, list[AppEventScreenshotField]]=None) -> AppEventScreenshotEndpoint:
        '''Fields to return for included related types.

        :param app_event_screenshot: the fields to include for returned resources of type appEventScreenshots
        :type app_event_screenshot: Union[AppEventScreenshotField, list[AppEventScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEventScreenshotEndpoint
        '''
        if app_event_screenshot: self._set_fields('appEventScreenshots',app_event_screenshot if type(app_event_screenshot) is list else [app_event_screenshot])
        return self
        
    class Include(StringEnum):
        APP_EVENT_LOCALIZATION = 'appEventLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> AppEventScreenshotEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEventScreenshotEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppEventScreenshotResponse:
        '''Get the resource.

        :returns: Single AppEventScreenshot
        :rtype: AppEventScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventScreenshotResponse.parse_obj(json)

    def update(self, request: AppEventScreenshotUpdateRequest) -> AppEventScreenshotResponse:
        '''Modify the resource.

        :param request: AppEventScreenshot representation
        :type request: AppEventScreenshotUpdateRequest

        :returns: Single AppEventScreenshot
        :rtype: AppEventScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppEventScreenshotResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

