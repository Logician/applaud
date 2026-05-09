from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppEventLocalizationsEndpoint(Endpoint):
    path = '/v1/appEventLocalizations'

    def create(self, request: AppEventLocalizationCreateRequest) -> AppEventLocalizationResponse:
        '''Create the resource.

        :param request: AppEventLocalization representation
        :type request: AppEventLocalizationCreateRequest

        :returns: Single AppEventLocalization
        :rtype: AppEventLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppEventLocalizationResponse.parse_obj(json)

class AppEventLocalizationEndpoint(IDEndpoint):
    path = '/v1/appEventLocalizations/{id}'

    @endpoint('/v1/appEventLocalizations/{id}/appEventScreenshots')
    def app_event_screenshots(self) -> AppEventScreenshotsOfAppEventLocalizationEndpoint:
        return AppEventScreenshotsOfAppEventLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appEventLocalizations/{id}/appEventVideoClips')
    def app_event_video_clips(self) -> AppEventVideoClipsOfAppEventLocalizationEndpoint:
        return AppEventVideoClipsOfAppEventLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appEventLocalizations/{id}/relationships/appEventScreenshots')
    def app_event_screenshots_linkages(self) -> AppEventScreenshotsLinkagesOfAppEventLocalizationEndpoint:
        return AppEventScreenshotsLinkagesOfAppEventLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appEventLocalizations/{id}/relationships/appEventVideoClips')
    def app_event_video_clips_linkages(self) -> AppEventVideoClipsLinkagesOfAppEventLocalizationEndpoint:
        return AppEventVideoClipsLinkagesOfAppEventLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]]=None, app_event_screenshot: Union[AppEventScreenshotField, list[AppEventScreenshotField]]=None, app_event_video_clip: Union[AppEventVideoClipField, list[AppEventVideoClipField]]=None) -> AppEventLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_event_localization: the fields to include for returned resources of type appEventLocalizations
        :type app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]] = None

        :param app_event_screenshot: the fields to include for returned resources of type appEventScreenshots
        :type app_event_screenshot: Union[AppEventScreenshotField, list[AppEventScreenshotField]] = None

        :param app_event_video_clip: the fields to include for returned resources of type appEventVideoClips
        :type app_event_video_clip: Union[AppEventVideoClipField, list[AppEventVideoClipField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEventLocalizationEndpoint
        '''
        if app_event_localization: self._set_fields('appEventLocalizations',app_event_localization if type(app_event_localization) is list else [app_event_localization])
        if app_event_screenshot: self._set_fields('appEventScreenshots',app_event_screenshot if type(app_event_screenshot) is list else [app_event_screenshot])
        if app_event_video_clip: self._set_fields('appEventVideoClips',app_event_video_clip if type(app_event_video_clip) is list else [app_event_video_clip])
        return self
        
    class Include(StringEnum):
        APP_EVENT = 'appEvent'
        APP_EVENT_SCREENSHOTS = 'appEventScreenshots'
        APP_EVENT_VIDEO_CLIPS = 'appEventVideoClips'

    def include(self, relationship: Union[Include, list[Include]]) -> AppEventLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEventLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_event_screenshots: int=None, app_event_video_clips: int=None) -> AppEventLocalizationEndpoint:
        '''Number of included related resources to return.

        :param app_event_screenshots: maximum number of related appEventScreenshots returned (when they are included). The maximum limit is 50
        :type app_event_screenshots: int = None

        :param app_event_video_clips: maximum number of related appEventVideoClips returned (when they are included). The maximum limit is 50
        :type app_event_video_clips: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEventLocalizationEndpoint
        '''
        if app_event_screenshots and app_event_screenshots > 50:
            raise ValueError(f'The maximum limit of app_event_screenshots is 50')
        if app_event_screenshots: self._set_limit(app_event_screenshots, 'appEventScreenshots')

        if app_event_video_clips and app_event_video_clips > 50:
            raise ValueError(f'The maximum limit of app_event_video_clips is 50')
        if app_event_video_clips: self._set_limit(app_event_video_clips, 'appEventVideoClips')

        return self

    def get(self) -> AppEventLocalizationResponse:
        '''Get the resource.

        :returns: Single AppEventLocalization
        :rtype: AppEventLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventLocalizationResponse.parse_obj(json)

    def update(self, request: AppEventLocalizationUpdateRequest) -> AppEventLocalizationResponse:
        '''Modify the resource.

        :param request: AppEventLocalization representation
        :type request: AppEventLocalizationUpdateRequest

        :returns: Single AppEventLocalization
        :rtype: AppEventLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppEventLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppEventScreenshotsLinkagesOfAppEventLocalizationEndpoint(IDEndpoint):
    path = '/v1/appEventLocalizations/{id}/relationships/appEventScreenshots'

    def limit(self, number: int=None) -> AppEventScreenshotsLinkagesOfAppEventLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEventScreenshotsLinkagesOfAppEventLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppEventLocalizationAppEventScreenshotsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppEventLocalizationAppEventScreenshotsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventLocalizationAppEventScreenshotsLinkagesResponse.parse_obj(json)

class AppEventScreenshotsOfAppEventLocalizationEndpoint(IDEndpoint):
    path = '/v1/appEventLocalizations/{id}/appEventScreenshots'

    def fields(self, *, app_event_screenshot: Union[AppEventScreenshotField, list[AppEventScreenshotField]]=None, app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]]=None) -> AppEventScreenshotsOfAppEventLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_event_screenshot: the fields to include for returned resources of type appEventScreenshots
        :type app_event_screenshot: Union[AppEventScreenshotField, list[AppEventScreenshotField]] = None

        :param app_event_localization: the fields to include for returned resources of type appEventLocalizations
        :type app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEventScreenshotsOfAppEventLocalizationEndpoint
        '''
        if app_event_screenshot: self._set_fields('appEventScreenshots',app_event_screenshot if type(app_event_screenshot) is list else [app_event_screenshot])
        if app_event_localization: self._set_fields('appEventLocalizations',app_event_localization if type(app_event_localization) is list else [app_event_localization])
        return self
        
    class Include(StringEnum):
        APP_EVENT_LOCALIZATION = 'appEventLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> AppEventScreenshotsOfAppEventLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEventScreenshotsOfAppEventLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AppEventScreenshotsOfAppEventLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEventScreenshotsOfAppEventLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppEventScreenshotsResponse:
        '''Get one or more resources.

        :returns: List of AppEventScreenshots
        :rtype: AppEventScreenshotsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventScreenshotsResponse.parse_obj(json)

class AppEventVideoClipsLinkagesOfAppEventLocalizationEndpoint(IDEndpoint):
    path = '/v1/appEventLocalizations/{id}/relationships/appEventVideoClips'

    def limit(self, number: int=None) -> AppEventVideoClipsLinkagesOfAppEventLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEventVideoClipsLinkagesOfAppEventLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppEventLocalizationAppEventVideoClipsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppEventLocalizationAppEventVideoClipsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventLocalizationAppEventVideoClipsLinkagesResponse.parse_obj(json)

class AppEventVideoClipsOfAppEventLocalizationEndpoint(IDEndpoint):
    path = '/v1/appEventLocalizations/{id}/appEventVideoClips'

    def fields(self, *, app_event_video_clip: Union[AppEventVideoClipField, list[AppEventVideoClipField]]=None, app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]]=None) -> AppEventVideoClipsOfAppEventLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_event_video_clip: the fields to include for returned resources of type appEventVideoClips
        :type app_event_video_clip: Union[AppEventVideoClipField, list[AppEventVideoClipField]] = None

        :param app_event_localization: the fields to include for returned resources of type appEventLocalizations
        :type app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEventVideoClipsOfAppEventLocalizationEndpoint
        '''
        if app_event_video_clip: self._set_fields('appEventVideoClips',app_event_video_clip if type(app_event_video_clip) is list else [app_event_video_clip])
        if app_event_localization: self._set_fields('appEventLocalizations',app_event_localization if type(app_event_localization) is list else [app_event_localization])
        return self
        
    class Include(StringEnum):
        APP_EVENT_LOCALIZATION = 'appEventLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> AppEventVideoClipsOfAppEventLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEventVideoClipsOfAppEventLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AppEventVideoClipsOfAppEventLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEventVideoClipsOfAppEventLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppEventVideoClipsResponse:
        '''Get one or more resources.

        :returns: List of AppEventVideoClips
        :rtype: AppEventVideoClipsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventVideoClipsResponse.parse_obj(json)

