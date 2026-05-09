from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ReviewSubmissionsEndpoint(Endpoint):
    path = '/v1/reviewSubmissions'

    class Platform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    class State(StringEnum):
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        UNRESOLVED_ISSUES = 'UNRESOLVED_ISSUES'
        CANCELING = 'CANCELING'
        COMPLETING = 'COMPLETING'
        COMPLETE = 'COMPLETE'

    def fields(self, *, review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]]=None, review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]]=None) -> ReviewSubmissionsEndpoint:
        '''Fields to return for included related types.

        :param review_submission: the fields to include for returned resources of type reviewSubmissions
        :type review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]] = None

        :param review_submission_item: the fields to include for returned resources of type reviewSubmissionItems
        :type review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsEndpoint
        '''
        if review_submission: self._set_fields('reviewSubmissions',review_submission if type(review_submission) is list else [review_submission])
        if review_submission_item: self._set_fields('reviewSubmissionItems',review_submission_item if type(review_submission_item) is list else [review_submission_item])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        ITEMS = 'items'
        APP_STORE_VERSION_FOR_REVIEW = 'appStoreVersionForReview'
        SUBMITTED_BY_ACTOR = 'submittedByActor'
        LAST_UPDATED_BY_ACTOR = 'lastUpdatedByActor'

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, state: Union[State, list[State]]=None, app: Union[str, list[str]]) -> ReviewSubmissionsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]]

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ReviewSubmissionsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, items: int=None) -> ReviewSubmissionsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param items: maximum number of related items returned (when they are included). The maximum limit is 50
        :type items: int = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if items and items > 50:
            raise ValueError(f'The maximum limit of items is 50')
        if items: self._set_limit(items, 'items')

        return self

    def get(self) -> ReviewSubmissionsResponse:
        '''Get one or more resources.

        :returns: List of ReviewSubmissions
        :rtype: ReviewSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ReviewSubmissionsResponse.parse_obj(json)

    def create(self, request: ReviewSubmissionCreateRequest) -> ReviewSubmissionResponse:
        '''Create the resource.

        :param request: ReviewSubmission representation
        :type request: ReviewSubmissionCreateRequest

        :returns: Single ReviewSubmission
        :rtype: ReviewSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return ReviewSubmissionResponse.parse_obj(json)

class ReviewSubmissionEndpoint(IDEndpoint):
    path = '/v1/reviewSubmissions/{id}'

    @endpoint('/v1/reviewSubmissions/{id}/items')
    def items(self) -> ItemsOfReviewSubmissionEndpoint:
        return ItemsOfReviewSubmissionEndpoint(self.id, self.session)
        
    @endpoint('/v1/reviewSubmissions/{id}/relationships/items')
    def items_linkages(self) -> ItemsLinkagesOfReviewSubmissionEndpoint:
        return ItemsLinkagesOfReviewSubmissionEndpoint(self.id, self.session)
        
    def fields(self, *, review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]]=None, review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]]=None) -> ReviewSubmissionEndpoint:
        '''Fields to return for included related types.

        :param review_submission: the fields to include for returned resources of type reviewSubmissions
        :type review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]] = None

        :param review_submission_item: the fields to include for returned resources of type reviewSubmissionItems
        :type review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionEndpoint
        '''
        if review_submission: self._set_fields('reviewSubmissions',review_submission if type(review_submission) is list else [review_submission])
        if review_submission_item: self._set_fields('reviewSubmissionItems',review_submission_item if type(review_submission_item) is list else [review_submission_item])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        ITEMS = 'items'
        APP_STORE_VERSION_FOR_REVIEW = 'appStoreVersionForReview'
        SUBMITTED_BY_ACTOR = 'submittedByActor'
        LAST_UPDATED_BY_ACTOR = 'lastUpdatedByActor'

    def include(self, relationship: Union[Include, list[Include]]) -> ReviewSubmissionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, items: int=None) -> ReviewSubmissionEndpoint:
        '''Number of included related resources to return.

        :param items: maximum number of related items returned (when they are included). The maximum limit is 50
        :type items: int = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionEndpoint
        '''
        if items and items > 50:
            raise ValueError(f'The maximum limit of items is 50')
        if items: self._set_limit(items, 'items')

        return self

    def get(self) -> ReviewSubmissionResponse:
        '''Get the resource.

        :returns: Single ReviewSubmission
        :rtype: ReviewSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ReviewSubmissionResponse.parse_obj(json)

    def update(self, request: ReviewSubmissionUpdateRequest) -> ReviewSubmissionResponse:
        '''Modify the resource.

        :param request: ReviewSubmission representation
        :type request: ReviewSubmissionUpdateRequest

        :returns: Single ReviewSubmission
        :rtype: ReviewSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return ReviewSubmissionResponse.parse_obj(json)

class ItemsLinkagesOfReviewSubmissionEndpoint(IDEndpoint):
    path = '/v1/reviewSubmissions/{id}/relationships/items'

    def limit(self, number: int=None) -> ItemsLinkagesOfReviewSubmissionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ItemsLinkagesOfReviewSubmissionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ReviewSubmissionItemsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: ReviewSubmissionItemsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ReviewSubmissionItemsLinkagesResponse.parse_obj(json)

class ItemsOfReviewSubmissionEndpoint(IDEndpoint):
    path = '/v1/reviewSubmissions/{id}/items'

    def fields(self, *, review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app_event: Union[AppEventField, list[AppEventField]]=None, background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]]=None, game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]]=None, game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]]=None, game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]]=None, game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]]=None, game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]]=None) -> ItemsOfReviewSubmissionEndpoint:
        '''Fields to return for included related types.

        :param review_submission_item: the fields to include for returned resources of type reviewSubmissionItems
        :type review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_custom_product_page_version: the fields to include for returned resources of type appCustomProductPageVersions
        :type app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]] = None

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param app_event: the fields to include for returned resources of type appEvents
        :type app_event: Union[AppEventField, list[AppEventField]] = None

        :param background_asset_version: the fields to include for returned resources of type backgroundAssetVersions
        :type background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]] = None

        :param game_center_achievement_version: the fields to include for returned resources of type gameCenterAchievementVersions
        :type game_center_achievement_version: Union[GameCenterAchievementVersionField, list[GameCenterAchievementVersionField]] = None

        :param game_center_activity_version: the fields to include for returned resources of type gameCenterActivityVersions
        :type game_center_activity_version: Union[GameCenterActivityVersionField, list[GameCenterActivityVersionField]] = None

        :param game_center_challenge_version: the fields to include for returned resources of type gameCenterChallengeVersions
        :type game_center_challenge_version: Union[GameCenterChallengeVersionField, list[GameCenterChallengeVersionField]] = None

        :param game_center_leaderboard_set_version: the fields to include for returned resources of type gameCenterLeaderboardSetVersions
        :type game_center_leaderboard_set_version: Union[GameCenterLeaderboardSetVersionField, list[GameCenterLeaderboardSetVersionField]] = None

        :param game_center_leaderboard_version: the fields to include for returned resources of type gameCenterLeaderboardVersions
        :type game_center_leaderboard_version: Union[GameCenterLeaderboardVersionField, list[GameCenterLeaderboardVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.ItemsOfReviewSubmissionEndpoint
        '''
        if review_submission_item: self._set_fields('reviewSubmissionItems',review_submission_item if type(review_submission_item) is list else [review_submission_item])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_custom_product_page_version: self._set_fields('appCustomProductPageVersions',app_custom_product_page_version if type(app_custom_product_page_version) is list else [app_custom_product_page_version])
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if app_event: self._set_fields('appEvents',app_event if type(app_event) is list else [app_event])
        if background_asset_version: self._set_fields('backgroundAssetVersions',background_asset_version if type(background_asset_version) is list else [background_asset_version])
        if game_center_achievement_version: self._set_fields('gameCenterAchievementVersions',game_center_achievement_version if type(game_center_achievement_version) is list else [game_center_achievement_version])
        if game_center_activity_version: self._set_fields('gameCenterActivityVersions',game_center_activity_version if type(game_center_activity_version) is list else [game_center_activity_version])
        if game_center_challenge_version: self._set_fields('gameCenterChallengeVersions',game_center_challenge_version if type(game_center_challenge_version) is list else [game_center_challenge_version])
        if game_center_leaderboard_set_version: self._set_fields('gameCenterLeaderboardSetVersions',game_center_leaderboard_set_version if type(game_center_leaderboard_set_version) is list else [game_center_leaderboard_set_version])
        if game_center_leaderboard_version: self._set_fields('gameCenterLeaderboardVersions',game_center_leaderboard_version if type(game_center_leaderboard_version) is list else [game_center_leaderboard_version])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'
        APP_CUSTOM_PRODUCT_PAGE_VERSION = 'appCustomProductPageVersion'
        APP_STORE_VERSION_EXPERIMENT = 'appStoreVersionExperiment'
        APP_STORE_VERSION_EXPERIMENT_V2 = 'appStoreVersionExperimentV2'
        APP_EVENT = 'appEvent'
        BACKGROUND_ASSET_VERSION = 'backgroundAssetVersion'
        GAME_CENTER_ACHIEVEMENT_VERSION = 'gameCenterAchievementVersion'
        GAME_CENTER_ACTIVITY_VERSION = 'gameCenterActivityVersion'
        GAME_CENTER_CHALLENGE_VERSION = 'gameCenterChallengeVersion'
        GAME_CENTER_LEADERBOARD_SET_VERSION = 'gameCenterLeaderboardSetVersion'
        GAME_CENTER_LEADERBOARD_VERSION = 'gameCenterLeaderboardVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> ItemsOfReviewSubmissionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ItemsOfReviewSubmissionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ItemsOfReviewSubmissionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ItemsOfReviewSubmissionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ReviewSubmissionItemsResponse:
        '''Get one or more resources.

        :returns: List of ReviewSubmissionItems
        :rtype: ReviewSubmissionItemsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ReviewSubmissionItemsResponse.parse_obj(json)

