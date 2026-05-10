from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class NominationsEndpoint(Endpoint):
    path = '/v1/nominations'

    class Type(StringEnum):
        APP_LAUNCH = 'APP_LAUNCH'
        APP_ENHANCEMENTS = 'APP_ENHANCEMENTS'
        NEW_CONTENT = 'NEW_CONTENT'

    class State(StringEnum):
        DRAFT = 'DRAFT'
        SUBMITTED = 'SUBMITTED'
        ARCHIVED = 'ARCHIVED'

    def fields(self, *, nomination: Union[NominationField, list[NominationField]]=None) -> NominationsEndpoint:
        '''Fields to return for included related types.

        :param nomination: the fields to include for returned resources of type nominations
        :type nomination: Union[NominationField, list[NominationField]] = None

        :returns: self
        :rtype: applaud.endpoints.NominationsEndpoint
        '''
        if nomination: self._set_fields('nominations',nomination if type(nomination) is list else [nomination])
        return self
        
    class Include(StringEnum):
        RELATED_APPS = 'relatedApps'
        CREATED_BY_ACTOR = 'createdByActor'
        LAST_MODIFIED_BY_ACTOR = 'lastModifiedByActor'
        SUBMITTED_BY_ACTOR = 'submittedByActor'
        IN_APP_EVENTS = 'inAppEvents'
        SUPPORTED_TERRITORIES = 'supportedTerritories'

    def exists(self, *, in_app_events: bool=None) -> NominationsEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.NominationsEndpoint
        '''
        if in_app_events == None:
            return
        
        self._set_exists('inAppEvents', 'true' if in_app_events  else 'false')
        return self
        
    def filter(self, *, type: Union[Type, list[Type]]=None, state: Union[State, list[State]], has_in_app_events: Union[str, list[str]]=None, related_apps: Union[str, list[str]]=None) -> NominationsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param type: filter by attribute 'type'
        :type type: Union[Type, list[Type]] = None

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]]

        :param has_in_app_events: filter by attribute 'hasInAppEvents'
        :type has_in_app_events: Union[str, list[str]] = None

        :param related_apps: filter by id(s) of related 'relatedApps'
        :type related_apps: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.NominationsEndpoint
        '''
        if type: self._set_filter('type', type if type(type) is list else [type])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        if has_in_app_events: self._set_filter('hasInAppEvents', has_in_app_events if type(has_in_app_events) is list else [has_in_app_events])
        
        if related_apps: self._set_filter('relatedApps', related_apps if type(related_apps) is list else [related_apps])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> NominationsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.NominationsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, last_modified_date: SortOrder=None, publish_start_date: SortOrder=None, publish_end_date: SortOrder=None, name: SortOrder=None, type: SortOrder=None) -> NominationsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.NominationsEndpoint
        '''
        if last_modified_date: self.sort_expressions.append('lastModifiedDate' if last_modified_date == SortOrder.ASC else '-lastModifiedDate')
        if publish_start_date: self.sort_expressions.append('publishStartDate' if publish_start_date == SortOrder.ASC else '-publishStartDate')
        if publish_end_date: self.sort_expressions.append('publishEndDate' if publish_end_date == SortOrder.ASC else '-publishEndDate')
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if type: self.sort_expressions.append('type' if type == SortOrder.ASC else '-type')
        return self
        
    def limit(self, number: int=None, *, in_app_events: int=None, related_apps: int=None, supported_territories: int=None) -> NominationsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param in_app_events: maximum number of related inAppEvents returned (when they are included). The maximum limit is 50
        :type in_app_events: int = None

        :param related_apps: maximum number of related relatedApps returned (when they are included). The maximum limit is 50
        :type related_apps: int = None

        :param supported_territories: maximum number of related supportedTerritories returned (when they are included). The maximum limit is 200
        :type supported_territories: int = None

        :returns: self
        :rtype: applaud.endpoints.NominationsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if in_app_events and in_app_events > 50:
            raise ValueError(f'The maximum limit of in_app_events is 50')
        if in_app_events: self._set_limit(in_app_events, 'inAppEvents')

        if related_apps and related_apps > 50:
            raise ValueError(f'The maximum limit of related_apps is 50')
        if related_apps: self._set_limit(related_apps, 'relatedApps')

        if supported_territories and supported_territories > 200:
            raise ValueError(f'The maximum limit of supported_territories is 200')
        if supported_territories: self._set_limit(supported_territories, 'supportedTerritories')

        return self

    def get(self) -> NominationsResponse:
        '''Get one or more resources.

        :returns: List of Nominations
        :rtype: NominationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return NominationsResponse.parse_obj(json)

    def get_all(self) -> NominationsResponse:
        '''
        Get all resources.

        :returns: List of Nominations
        :rtype: NominationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = NominationsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = NominationsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def create(self, request: NominationCreateRequest) -> NominationResponse:
        '''Create the resource.

        :param request: Nomination representation
        :type request: NominationCreateRequest

        :returns: Single Nomination
        :rtype: NominationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return NominationResponse.parse_obj(json)

class NominationEndpoint(IDEndpoint):
    path = '/v1/nominations/{id}'

    def fields(self, *, nomination: Union[NominationField, list[NominationField]]=None) -> NominationEndpoint:
        '''Fields to return for included related types.

        :param nomination: the fields to include for returned resources of type nominations
        :type nomination: Union[NominationField, list[NominationField]] = None

        :returns: self
        :rtype: applaud.endpoints.NominationEndpoint
        '''
        if nomination: self._set_fields('nominations',nomination if type(nomination) is list else [nomination])
        return self
        
    class Include(StringEnum):
        RELATED_APPS = 'relatedApps'
        CREATED_BY_ACTOR = 'createdByActor'
        LAST_MODIFIED_BY_ACTOR = 'lastModifiedByActor'
        SUBMITTED_BY_ACTOR = 'submittedByActor'
        IN_APP_EVENTS = 'inAppEvents'
        SUPPORTED_TERRITORIES = 'supportedTerritories'

    def include(self, relationship: Union[Include, list[Include]]) -> NominationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.NominationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, in_app_events: int=None, related_apps: int=None, supported_territories: int=None) -> NominationEndpoint:
        '''Number of included related resources to return.

        :param in_app_events: maximum number of related inAppEvents returned (when they are included). The maximum limit is 50
        :type in_app_events: int = None

        :param related_apps: maximum number of related relatedApps returned (when they are included). The maximum limit is 50
        :type related_apps: int = None

        :param supported_territories: maximum number of related supportedTerritories returned (when they are included). The maximum limit is 200
        :type supported_territories: int = None

        :returns: self
        :rtype: applaud.endpoints.NominationEndpoint
        '''
        if in_app_events and in_app_events > 50:
            raise ValueError(f'The maximum limit of in_app_events is 50')
        if in_app_events: self._set_limit(in_app_events, 'inAppEvents')

        if related_apps and related_apps > 50:
            raise ValueError(f'The maximum limit of related_apps is 50')
        if related_apps: self._set_limit(related_apps, 'relatedApps')

        if supported_territories and supported_territories > 200:
            raise ValueError(f'The maximum limit of supported_territories is 200')
        if supported_territories: self._set_limit(supported_territories, 'supportedTerritories')

        return self

    def get(self) -> NominationResponse:
        '''Get the resource.

        :returns: Single Nomination
        :rtype: NominationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return NominationResponse.parse_obj(json)

    def get_all(self) -> NominationResponse:
        '''
        Get all resources.

        :returns: Single Nomination
        :rtype: NominationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = NominationResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = NominationResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def update(self, request: NominationUpdateRequest) -> NominationResponse:
        '''Modify the resource.

        :param request: Nomination representation
        :type request: NominationUpdateRequest

        :returns: Single Nomination
        :rtype: NominationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return NominationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

