from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionGroupsEndpoint(Endpoint):
    path = '/v1/subscriptionGroups'

    def create(self, request: SubscriptionGroupCreateRequest) -> SubscriptionGroupResponse:
        '''Create the resource.

        :param request: SubscriptionGroup representation
        :type request: SubscriptionGroupCreateRequest

        :returns: Single SubscriptionGroup
        :rtype: SubscriptionGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionGroupResponse.parse_obj(json)

class SubscriptionGroupEndpoint(IDEndpoint):
    path = '/v1/subscriptionGroups/{id}'

    @endpoint('/v1/subscriptionGroups/{id}/subscriptionGroupLocalizations')
    def subscription_group_localizations(self) -> SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint:
        return SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionGroups/{id}/subscriptions')
    def subscriptions(self) -> SubscriptionsOfSubscriptionGroupEndpoint:
        return SubscriptionsOfSubscriptionGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionGroups/{id}/relationships/subscriptionGroupLocalizations')
    def subscription_group_localizations_linkages(self) -> SubscriptionGroupLocalizationsLinkagesOfSubscriptionGroupEndpoint:
        return SubscriptionGroupLocalizationsLinkagesOfSubscriptionGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionGroups/{id}/relationships/subscriptions')
    def subscriptions_linkages(self) -> SubscriptionsLinkagesOfSubscriptionGroupEndpoint:
        return SubscriptionsLinkagesOfSubscriptionGroupEndpoint(self.id, self.session)
        
    def fields(self, *, subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None, subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]]=None) -> SubscriptionGroupEndpoint:
        '''Fields to return for included related types.

        :param subscription_group: the fields to include for returned resources of type subscriptionGroups
        :type subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :param subscription_group_localization: the fields to include for returned resources of type subscriptionGroupLocalizations
        :type subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupEndpoint
        '''
        if subscription_group: self._set_fields('subscriptionGroups',subscription_group if type(subscription_group) is list else [subscription_group])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        if subscription_group_localization: self._set_fields('subscriptionGroupLocalizations',subscription_group_localization if type(subscription_group_localization) is list else [subscription_group_localization])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTIONS = 'subscriptions'
        SUBSCRIPTION_GROUP_LOCALIZATIONS = 'subscriptionGroupLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, subscription_group_localizations: int=None, subscriptions: int=None) -> SubscriptionGroupEndpoint:
        '''Number of included related resources to return.

        :param subscription_group_localizations: maximum number of related subscriptionGroupLocalizations returned (when they are included). The maximum limit is 50
        :type subscription_group_localizations: int = None

        :param subscriptions: maximum number of related subscriptions returned (when they are included). The maximum limit is 50
        :type subscriptions: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupEndpoint
        '''
        if subscription_group_localizations and subscription_group_localizations > 50:
            raise ValueError(f'The maximum limit of subscription_group_localizations is 50')
        if subscription_group_localizations: self._set_limit(subscription_group_localizations, 'subscriptionGroupLocalizations')

        if subscriptions and subscriptions > 50:
            raise ValueError(f'The maximum limit of subscriptions is 50')
        if subscriptions: self._set_limit(subscriptions, 'subscriptions')

        return self

    def get(self) -> SubscriptionGroupResponse:
        '''Get the resource.

        :returns: Single SubscriptionGroup
        :rtype: SubscriptionGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGroupResponse.parse_obj(json)

    def update(self, request: SubscriptionGroupUpdateRequest) -> SubscriptionGroupResponse:
        '''Modify the resource.

        :param request: SubscriptionGroup representation
        :type request: SubscriptionGroupUpdateRequest

        :returns: Single SubscriptionGroup
        :rtype: SubscriptionGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionGroupResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class SubscriptionGroupLocalizationsLinkagesOfSubscriptionGroupEndpoint(IDEndpoint):
    path = '/v1/subscriptionGroups/{id}/relationships/subscriptionGroupLocalizations'

    def limit(self, number: int=None) -> SubscriptionGroupLocalizationsLinkagesOfSubscriptionGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupLocalizationsLinkagesOfSubscriptionGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse.parse_obj(json)

class SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint(IDEndpoint):
    path = '/v1/subscriptionGroups/{id}/subscriptionGroupLocalizations'

    def fields(self, *, subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]]=None, subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]]=None) -> SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint:
        '''Fields to return for included related types.

        :param subscription_group_localization: the fields to include for returned resources of type subscriptionGroupLocalizations
        :type subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]] = None

        :param subscription_group: the fields to include for returned resources of type subscriptionGroups
        :type subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint
        '''
        if subscription_group_localization: self._set_fields('subscriptionGroupLocalizations',subscription_group_localization if type(subscription_group_localization) is list else [subscription_group_localization])
        if subscription_group: self._set_fields('subscriptionGroups',subscription_group if type(subscription_group) is list else [subscription_group])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION_GROUP = 'subscriptionGroup'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupLocalizationsOfSubscriptionGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionGroupLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionGroupLocalizations
        :rtype: SubscriptionGroupLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGroupLocalizationsResponse.parse_obj(json)

class SubscriptionsLinkagesOfSubscriptionGroupEndpoint(IDEndpoint):
    path = '/v1/subscriptionGroups/{id}/relationships/subscriptions'

    def limit(self, number: int=None) -> SubscriptionsLinkagesOfSubscriptionGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionsLinkagesOfSubscriptionGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionGroupSubscriptionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionGroupSubscriptionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGroupSubscriptionsLinkagesResponse.parse_obj(json)

class SubscriptionsOfSubscriptionGroupEndpoint(IDEndpoint):
    path = '/v1/subscriptionGroups/{id}/subscriptions'

    class State(StringEnum):
        MISSING_METADATA = 'MISSING_METADATA'
        READY_TO_SUBMIT = 'READY_TO_SUBMIT'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        DEVELOPER_ACTION_NEEDED = 'DEVELOPER_ACTION_NEEDED'
        PENDING_BINARY_APPROVAL = 'PENDING_BINARY_APPROVAL'
        APPROVED = 'APPROVED'
        DEVELOPER_REMOVED_FROM_SALE = 'DEVELOPER_REMOVED_FROM_SALE'
        REMOVED_FROM_SALE = 'REMOVED_FROM_SALE'
        REJECTED = 'REJECTED'

    def fields(self, *, subscription: Union[SubscriptionField, list[SubscriptionField]]=None, subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]]=None, subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]]=None, subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]]=None, subscription_introductory_offer: Union[SubscriptionIntroductoryOfferField, list[SubscriptionIntroductoryOfferField]]=None, subscription_promotional_offer: Union[SubscriptionPromotionalOfferField, list[SubscriptionPromotionalOfferField]]=None, subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]]=None, subscription_price: Union[SubscriptionPriceField, list[SubscriptionPriceField]]=None, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, subscription_availability: Union[SubscriptionAvailabilityField, list[SubscriptionAvailabilityField]]=None, win_back_offer: Union[WinBackOfferField, list[WinBackOfferField]]=None, subscription_image: Union[SubscriptionImageField, list[SubscriptionImageField]]=None) -> SubscriptionsOfSubscriptionGroupEndpoint:
        '''Fields to return for included related types.

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :param subscription_localization: the fields to include for returned resources of type subscriptionLocalizations
        :type subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]] = None

        :param subscription_app_store_review_screenshot: the fields to include for returned resources of type subscriptionAppStoreReviewScreenshots
        :type subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]] = None

        :param subscription_group: the fields to include for returned resources of type subscriptionGroups
        :type subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]] = None

        :param subscription_introductory_offer: the fields to include for returned resources of type subscriptionIntroductoryOffers
        :type subscription_introductory_offer: Union[SubscriptionIntroductoryOfferField, list[SubscriptionIntroductoryOfferField]] = None

        :param subscription_promotional_offer: the fields to include for returned resources of type subscriptionPromotionalOffers
        :type subscription_promotional_offer: Union[SubscriptionPromotionalOfferField, list[SubscriptionPromotionalOfferField]] = None

        :param subscription_offer_code: the fields to include for returned resources of type subscriptionOfferCodes
        :type subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]] = None

        :param subscription_price: the fields to include for returned resources of type subscriptionPrices
        :type subscription_price: Union[SubscriptionPriceField, list[SubscriptionPriceField]] = None

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :param subscription_availability: the fields to include for returned resources of type subscriptionAvailabilities
        :type subscription_availability: Union[SubscriptionAvailabilityField, list[SubscriptionAvailabilityField]] = None

        :param win_back_offer: the fields to include for returned resources of type winBackOffers
        :type win_back_offer: Union[WinBackOfferField, list[WinBackOfferField]] = None

        :param subscription_image: the fields to include for returned resources of type subscriptionImages
        :type subscription_image: Union[SubscriptionImageField, list[SubscriptionImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionsOfSubscriptionGroupEndpoint
        '''
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        if subscription_localization: self._set_fields('subscriptionLocalizations',subscription_localization if type(subscription_localization) is list else [subscription_localization])
        if subscription_app_store_review_screenshot: self._set_fields('subscriptionAppStoreReviewScreenshots',subscription_app_store_review_screenshot if type(subscription_app_store_review_screenshot) is list else [subscription_app_store_review_screenshot])
        if subscription_group: self._set_fields('subscriptionGroups',subscription_group if type(subscription_group) is list else [subscription_group])
        if subscription_introductory_offer: self._set_fields('subscriptionIntroductoryOffers',subscription_introductory_offer if type(subscription_introductory_offer) is list else [subscription_introductory_offer])
        if subscription_promotional_offer: self._set_fields('subscriptionPromotionalOffers',subscription_promotional_offer if type(subscription_promotional_offer) is list else [subscription_promotional_offer])
        if subscription_offer_code: self._set_fields('subscriptionOfferCodes',subscription_offer_code if type(subscription_offer_code) is list else [subscription_offer_code])
        if subscription_price: self._set_fields('subscriptionPrices',subscription_price if type(subscription_price) is list else [subscription_price])
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        if subscription_availability: self._set_fields('subscriptionAvailabilities',subscription_availability if type(subscription_availability) is list else [subscription_availability])
        if win_back_offer: self._set_fields('winBackOffers',win_back_offer if type(win_back_offer) is list else [win_back_offer])
        if subscription_image: self._set_fields('subscriptionImages',subscription_image if type(subscription_image) is list else [subscription_image])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION_LOCALIZATIONS = 'subscriptionLocalizations'
        APP_STORE_REVIEW_SCREENSHOT = 'appStoreReviewScreenshot'
        GROUP = 'group'
        INTRODUCTORY_OFFERS = 'introductoryOffers'
        PROMOTIONAL_OFFERS = 'promotionalOffers'
        OFFER_CODES = 'offerCodes'
        PRICES = 'prices'
        PROMOTED_PURCHASE = 'promotedPurchase'
        SUBSCRIPTION_AVAILABILITY = 'subscriptionAvailability'
        WIN_BACK_OFFERS = 'winBackOffers'
        IMAGES = 'images'

    def filter(self, *, product_id: Union[str, list[str]]=None, name: Union[str, list[str]]=None, state: Union[State, list[State]]=None) -> SubscriptionsOfSubscriptionGroupEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param product_id: filter by attribute 'productId'
        :type product_id: Union[str, list[str]] = None

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionsOfSubscriptionGroupEndpoint
        '''
        if product_id: self._set_filter('productId', product_id if type(product_id) is list else [product_id])
        
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionsOfSubscriptionGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionsOfSubscriptionGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None) -> SubscriptionsOfSubscriptionGroupEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionsOfSubscriptionGroupEndpoint
        '''
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        return self
        
    def limit(self, number: int=None, *, subscription_localizations: int=None, introductory_offers: int=None, promotional_offers: int=None, offer_codes: int=None, prices: int=None, win_back_offers: int=None, images: int=None) -> SubscriptionsOfSubscriptionGroupEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param subscription_localizations: maximum number of related subscriptionLocalizations returned (when they are included). The maximum limit is 50
        :type subscription_localizations: int = None

        :param introductory_offers: maximum number of related introductoryOffers returned (when they are included). The maximum limit is 50
        :type introductory_offers: int = None

        :param promotional_offers: maximum number of related promotionalOffers returned (when they are included). The maximum limit is 50
        :type promotional_offers: int = None

        :param offer_codes: maximum number of related offerCodes returned (when they are included). The maximum limit is 50
        :type offer_codes: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :param win_back_offers: maximum number of related winBackOffers returned (when they are included). The maximum limit is 50
        :type win_back_offers: int = None

        :param images: maximum number of related images returned (when they are included). The maximum limit is 50
        :type images: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionsOfSubscriptionGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if subscription_localizations and subscription_localizations > 50:
            raise ValueError(f'The maximum limit of subscription_localizations is 50')
        if subscription_localizations: self._set_limit(subscription_localizations, 'subscriptionLocalizations')

        if introductory_offers and introductory_offers > 50:
            raise ValueError(f'The maximum limit of introductory_offers is 50')
        if introductory_offers: self._set_limit(introductory_offers, 'introductoryOffers')

        if promotional_offers and promotional_offers > 50:
            raise ValueError(f'The maximum limit of promotional_offers is 50')
        if promotional_offers: self._set_limit(promotional_offers, 'promotionalOffers')

        if offer_codes and offer_codes > 50:
            raise ValueError(f'The maximum limit of offer_codes is 50')
        if offer_codes: self._set_limit(offer_codes, 'offerCodes')

        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        if win_back_offers and win_back_offers > 50:
            raise ValueError(f'The maximum limit of win_back_offers is 50')
        if win_back_offers: self._set_limit(win_back_offers, 'winBackOffers')

        if images and images > 50:
            raise ValueError(f'The maximum limit of images is 50')
        if images: self._set_limit(images, 'images')

        return self

    def get(self) -> SubscriptionsResponse:
        '''Get one or more resources.

        :returns: List of Subscriptions
        :rtype: SubscriptionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionsResponse.parse_obj(json)

