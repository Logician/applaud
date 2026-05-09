from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppEventVideoClipsEndpoint(Endpoint):
    path = '/v1/appEventVideoClips'

    def create(self, request: AppEventVideoClipCreateRequest) -> AppEventVideoClipResponse:
        '''Create the resource.

        :param request: AppEventVideoClip representation
        :type request: AppEventVideoClipCreateRequest

        :returns: Single AppEventVideoClip
        :rtype: AppEventVideoClipResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppEventVideoClipResponse.parse_obj(json)

class AppEventVideoClipEndpoint(IDEndpoint):
    path = '/v1/appEventVideoClips/{id}'

    def fields(self, *, app_event_video_clip: Union[AppEventVideoClipField, list[AppEventVideoClipField]]=None) -> AppEventVideoClipEndpoint:
        '''Fields to return for included related types.

        :param app_event_video_clip: the fields to include for returned resources of type appEventVideoClips
        :type app_event_video_clip: Union[AppEventVideoClipField, list[AppEventVideoClipField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEventVideoClipEndpoint
        '''
        if app_event_video_clip: self._set_fields('appEventVideoClips',app_event_video_clip if type(app_event_video_clip) is list else [app_event_video_clip])
        return self
        
    class Include(StringEnum):
        APP_EVENT_LOCALIZATION = 'appEventLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> AppEventVideoClipEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEventVideoClipEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppEventVideoClipResponse:
        '''Get the resource.

        :returns: Single AppEventVideoClip
        :rtype: AppEventVideoClipResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventVideoClipResponse.parse_obj(json)

    def update(self, request: AppEventVideoClipUpdateRequest) -> AppEventVideoClipResponse:
        '''Modify the resource.

        :param request: AppEventVideoClip representation
        :type request: AppEventVideoClipUpdateRequest

        :returns: Single AppEventVideoClip
        :rtype: AppEventVideoClipResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppEventVideoClipResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

