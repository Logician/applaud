from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionsEndpoint(Endpoint):
    path = '/v1/subscriptions'

    def create(self, request: SubscriptionCreateRequest) -> SubscriptionResponse:
        '''Create the resource.

        :param request: Subscription representation
        :type request: SubscriptionCreateRequest

        :returns: Single Subscription
        :rtype: SubscriptionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionResponse.parse_obj(json)

class SubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}'

    @endpoint('/v1/subscriptions/{id}/appStoreReviewScreenshot')
    def app_store_review_screenshot(self) -> AppStoreReviewScreenshotOfSubscriptionEndpoint:
        return AppStoreReviewScreenshotOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/images')
    def images(self) -> ImagesOfSubscriptionEndpoint:
        return ImagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/introductoryOffers')
    def introductory_offers(self) -> IntroductoryOffersOfSubscriptionEndpoint:
        return IntroductoryOffersOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/offerCodes')
    def offer_codes(self) -> OfferCodesOfSubscriptionEndpoint:
        return OfferCodesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/pricePoints')
    def price_points(self) -> PricePointsOfSubscriptionEndpoint:
        return PricePointsOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/prices')
    def prices(self) -> PricesOfSubscriptionEndpoint:
        return PricesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/promotedPurchase')
    def promoted_purchase(self) -> PromotedPurchaseOfSubscriptionEndpoint:
        return PromotedPurchaseOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/promotionalOffers')
    def promotional_offers(self) -> PromotionalOffersOfSubscriptionEndpoint:
        return PromotionalOffersOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/subscriptionAvailability')
    def subscription_availability(self) -> SubscriptionAvailabilityOfSubscriptionEndpoint:
        return SubscriptionAvailabilityOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/subscriptionLocalizations')
    def subscription_localizations(self) -> SubscriptionLocalizationsOfSubscriptionEndpoint:
        return SubscriptionLocalizationsOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/winBackOffers')
    def win_back_offers(self) -> WinBackOffersOfSubscriptionEndpoint:
        return WinBackOffersOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/appStoreReviewScreenshot')
    def app_store_review_screenshot_linkage(self) -> AppStoreReviewScreenshotLinkageOfSubscriptionEndpoint:
        return AppStoreReviewScreenshotLinkageOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/images')
    def images_linkages(self) -> ImagesLinkagesOfSubscriptionEndpoint:
        return ImagesLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/introductoryOffers')
    def introductory_offers_linkages(self) -> IntroductoryOffersLinkagesOfSubscriptionEndpoint:
        return IntroductoryOffersLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/offerCodes')
    def offer_codes_linkages(self) -> OfferCodesLinkagesOfSubscriptionEndpoint:
        return OfferCodesLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/pricePoints')
    def price_points_linkages(self) -> PricePointsLinkagesOfSubscriptionEndpoint:
        return PricePointsLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/prices')
    def prices_linkages(self) -> PricesLinkagesOfSubscriptionEndpoint:
        return PricesLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/promotedPurchase')
    def promoted_purchase_linkage(self) -> PromotedPurchaseLinkageOfSubscriptionEndpoint:
        return PromotedPurchaseLinkageOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/promotionalOffers')
    def promotional_offers_linkages(self) -> PromotionalOffersLinkagesOfSubscriptionEndpoint:
        return PromotionalOffersLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/subscriptionAvailability')
    def subscription_availability_linkage(self) -> SubscriptionAvailabilityLinkageOfSubscriptionEndpoint:
        return SubscriptionAvailabilityLinkageOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/subscriptionLocalizations')
    def subscription_localizations_linkages(self) -> SubscriptionLocalizationsLinkagesOfSubscriptionEndpoint:
        return SubscriptionLocalizationsLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptions/{id}/relationships/winBackOffers')
    def win_back_offers_linkages(self) -> WinBackOffersLinkagesOfSubscriptionEndpoint:
        return WinBackOffersLinkagesOfSubscriptionEndpoint(self.id, self.session)
        
    def fields(self, *, subscription: Union[SubscriptionField, list[SubscriptionField]]=None, subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]]=None, subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]]=None, subscription_introductory_offer: Union[SubscriptionIntroductoryOfferField, list[SubscriptionIntroductoryOfferField]]=None, subscription_promotional_offer: Union[SubscriptionPromotionalOfferField, list[SubscriptionPromotionalOfferField]]=None, subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]]=None, subscription_price: Union[SubscriptionPriceField, list[SubscriptionPriceField]]=None, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, subscription_availability: Union[SubscriptionAvailabilityField, list[SubscriptionAvailabilityField]]=None, win_back_offer: Union[WinBackOfferField, list[WinBackOfferField]]=None, subscription_image: Union[SubscriptionImageField, list[SubscriptionImageField]]=None) -> SubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :param subscription_localization: the fields to include for returned resources of type subscriptionLocalizations
        :type subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]] = None

        :param subscription_app_store_review_screenshot: the fields to include for returned resources of type subscriptionAppStoreReviewScreenshots
        :type subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]] = None

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
        :rtype: applaud.endpoints.SubscriptionEndpoint
        '''
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        if subscription_localization: self._set_fields('subscriptionLocalizations',subscription_localization if type(subscription_localization) is list else [subscription_localization])
        if subscription_app_store_review_screenshot: self._set_fields('subscriptionAppStoreReviewScreenshots',subscription_app_store_review_screenshot if type(subscription_app_store_review_screenshot) is list else [subscription_app_store_review_screenshot])
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

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, images: int=None, introductory_offers: int=None, offer_codes: int=None, prices: int=None, promotional_offers: int=None, subscription_localizations: int=None, win_back_offers: int=None) -> SubscriptionEndpoint:
        '''Number of included related resources to return.

        :param images: maximum number of related images returned (when they are included). The maximum limit is 50
        :type images: int = None

        :param introductory_offers: maximum number of related introductoryOffers returned (when they are included). The maximum limit is 50
        :type introductory_offers: int = None

        :param offer_codes: maximum number of related offerCodes returned (when they are included). The maximum limit is 50
        :type offer_codes: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :param promotional_offers: maximum number of related promotionalOffers returned (when they are included). The maximum limit is 50
        :type promotional_offers: int = None

        :param subscription_localizations: maximum number of related subscriptionLocalizations returned (when they are included). The maximum limit is 50
        :type subscription_localizations: int = None

        :param win_back_offers: maximum number of related winBackOffers returned (when they are included). The maximum limit is 50
        :type win_back_offers: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionEndpoint
        '''
        if images and images > 50:
            raise ValueError(f'The maximum limit of images is 50')
        if images: self._set_limit(images, 'images')

        if introductory_offers and introductory_offers > 50:
            raise ValueError(f'The maximum limit of introductory_offers is 50')
        if introductory_offers: self._set_limit(introductory_offers, 'introductoryOffers')

        if offer_codes and offer_codes > 50:
            raise ValueError(f'The maximum limit of offer_codes is 50')
        if offer_codes: self._set_limit(offer_codes, 'offerCodes')

        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        if promotional_offers and promotional_offers > 50:
            raise ValueError(f'The maximum limit of promotional_offers is 50')
        if promotional_offers: self._set_limit(promotional_offers, 'promotionalOffers')

        if subscription_localizations and subscription_localizations > 50:
            raise ValueError(f'The maximum limit of subscription_localizations is 50')
        if subscription_localizations: self._set_limit(subscription_localizations, 'subscriptionLocalizations')

        if win_back_offers and win_back_offers > 50:
            raise ValueError(f'The maximum limit of win_back_offers is 50')
        if win_back_offers: self._set_limit(win_back_offers, 'winBackOffers')

        return self

    def get(self) -> SubscriptionResponse:
        '''Get the resource.

        :returns: Single Subscription
        :rtype: SubscriptionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionResponse.parse_obj(json)

    def update(self, request: SubscriptionUpdateRequest) -> SubscriptionResponse:
        '''Modify the resource.

        :param request: Subscription representation
        :type request: SubscriptionUpdateRequest

        :returns: Single Subscription
        :rtype: SubscriptionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppStoreReviewScreenshotLinkageOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/appStoreReviewScreenshot'

    def get(self) -> SubscriptionAppStoreReviewScreenshotLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: SubscriptionAppStoreReviewScreenshotLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionAppStoreReviewScreenshotLinkageResponse.parse_obj(json)

class AppStoreReviewScreenshotOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/appStoreReviewScreenshot'

    def fields(self, *, subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None) -> AppStoreReviewScreenshotOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_app_store_review_screenshot: the fields to include for returned resources of type subscriptionAppStoreReviewScreenshots
        :type subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewScreenshotOfSubscriptionEndpoint
        '''
        if subscription_app_store_review_screenshot: self._set_fields('subscriptionAppStoreReviewScreenshots',subscription_app_store_review_screenshot if type(subscription_app_store_review_screenshot) is list else [subscription_app_store_review_screenshot])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreReviewScreenshotOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewScreenshotOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionAppStoreReviewScreenshotResponse:
        '''Get the resource.

        :returns: Single SubscriptionAppStoreReviewScreenshot
        :rtype: SubscriptionAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionAppStoreReviewScreenshotResponse.parse_obj(json)

class ImagesLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/images'

    def limit(self, number: int=None) -> ImagesLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ImagesLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionImagesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionImagesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionImagesLinkagesResponse.parse_obj(json)

class ImagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/images'

    def fields(self, *, subscription_image: Union[SubscriptionImageField, list[SubscriptionImageField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None) -> ImagesOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_image: the fields to include for returned resources of type subscriptionImages
        :type subscription_image: Union[SubscriptionImageField, list[SubscriptionImageField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :returns: self
        :rtype: applaud.endpoints.ImagesOfSubscriptionEndpoint
        '''
        if subscription_image: self._set_fields('subscriptionImages',subscription_image if type(subscription_image) is list else [subscription_image])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> ImagesOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ImagesOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ImagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ImagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionImagesResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionImages
        :rtype: SubscriptionImagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionImagesResponse.parse_obj(json)

class IntroductoryOffersLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/introductoryOffers'

    def limit(self, number: int=None) -> IntroductoryOffersLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IntroductoryOffersLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionIntroductoryOffersLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionIntroductoryOffersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionIntroductoryOffersLinkagesResponse.parse_obj(json)

    def delete(self, request: SubscriptionIntroductoryOffersLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: SubscriptionIntroductoryOffersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class IntroductoryOffersOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/introductoryOffers'

    def fields(self, *, subscription_introductory_offer: Union[SubscriptionIntroductoryOfferField, list[SubscriptionIntroductoryOfferField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None) -> IntroductoryOffersOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_introductory_offer: the fields to include for returned resources of type subscriptionIntroductoryOffers
        :type subscription_introductory_offer: Union[SubscriptionIntroductoryOfferField, list[SubscriptionIntroductoryOfferField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.IntroductoryOffersOfSubscriptionEndpoint
        '''
        if subscription_introductory_offer: self._set_fields('subscriptionIntroductoryOffers',subscription_introductory_offer if type(subscription_introductory_offer) is list else [subscription_introductory_offer])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'
        TERRITORY = 'territory'
        SUBSCRIPTION_PRICE_POINT = 'subscriptionPricePoint'

    def filter(self, *, territory: Union[str, list[str]]=None) -> IntroductoryOffersOfSubscriptionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.IntroductoryOffersOfSubscriptionEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> IntroductoryOffersOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.IntroductoryOffersOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> IntroductoryOffersOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IntroductoryOffersOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionIntroductoryOffersResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionIntroductoryOffers
        :rtype: SubscriptionIntroductoryOffersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionIntroductoryOffersResponse.parse_obj(json)

class OfferCodesLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/offerCodes'

    def limit(self, number: int=None) -> OfferCodesLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.OfferCodesLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionOfferCodesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionOfferCodesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodesLinkagesResponse.parse_obj(json)

class OfferCodesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/offerCodes'

    def fields(self, *, subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None, subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]]=None, subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]]=None, subscription_offer_code_price: Union[SubscriptionOfferCodePriceField, list[SubscriptionOfferCodePriceField]]=None) -> OfferCodesOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_offer_code: the fields to include for returned resources of type subscriptionOfferCodes
        :type subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :param subscription_offer_code_one_time_use_code: the fields to include for returned resources of type subscriptionOfferCodeOneTimeUseCodes
        :type subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]] = None

        :param subscription_offer_code_custom_code: the fields to include for returned resources of type subscriptionOfferCodeCustomCodes
        :type subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]] = None

        :param subscription_offer_code_price: the fields to include for returned resources of type subscriptionOfferCodePrices
        :type subscription_offer_code_price: Union[SubscriptionOfferCodePriceField, list[SubscriptionOfferCodePriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.OfferCodesOfSubscriptionEndpoint
        '''
        if subscription_offer_code: self._set_fields('subscriptionOfferCodes',subscription_offer_code if type(subscription_offer_code) is list else [subscription_offer_code])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        if subscription_offer_code_one_time_use_code: self._set_fields('subscriptionOfferCodeOneTimeUseCodes',subscription_offer_code_one_time_use_code if type(subscription_offer_code_one_time_use_code) is list else [subscription_offer_code_one_time_use_code])
        if subscription_offer_code_custom_code: self._set_fields('subscriptionOfferCodeCustomCodes',subscription_offer_code_custom_code if type(subscription_offer_code_custom_code) is list else [subscription_offer_code_custom_code])
        if subscription_offer_code_price: self._set_fields('subscriptionOfferCodePrices',subscription_offer_code_price if type(subscription_offer_code_price) is list else [subscription_offer_code_price])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'
        ONE_TIME_USE_CODES = 'oneTimeUseCodes'
        CUSTOM_CODES = 'customCodes'
        PRICES = 'prices'

    def filter(self, *, territory: Union[str, list[str]]=None) -> OfferCodesOfSubscriptionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by territory
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.OfferCodesOfSubscriptionEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> OfferCodesOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.OfferCodesOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, one_time_use_codes: int=None, custom_codes: int=None, prices: int=None) -> OfferCodesOfSubscriptionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param one_time_use_codes: maximum number of related oneTimeUseCodes returned (when they are included). The maximum limit is 50
        :type one_time_use_codes: int = None

        :param custom_codes: maximum number of related customCodes returned (when they are included). The maximum limit is 50
        :type custom_codes: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.OfferCodesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if one_time_use_codes and one_time_use_codes > 50:
            raise ValueError(f'The maximum limit of one_time_use_codes is 50')
        if one_time_use_codes: self._set_limit(one_time_use_codes, 'oneTimeUseCodes')

        if custom_codes and custom_codes > 50:
            raise ValueError(f'The maximum limit of custom_codes is 50')
        if custom_codes: self._set_limit(custom_codes, 'customCodes')

        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        return self

    def get(self) -> SubscriptionOfferCodesResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionOfferCodes
        :rtype: SubscriptionOfferCodesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodesResponse.parse_obj(json)

class PricePointsLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/pricePoints'

    def limit(self, number: int=None) -> PricePointsLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPricePointsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionPricePointsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPricePointsLinkagesResponse.parse_obj(json)

class PricePointsOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/pricePoints'

    def fields(self, *, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> PricePointsOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfSubscriptionEndpoint
        '''
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None) -> PricePointsOfSubscriptionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfSubscriptionEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PricePointsOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PricePointsOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfSubscriptionEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPricePointsResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionPricePoints
        :rtype: SubscriptionPricePointsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPricePointsResponse.parse_obj(json)

class PricesLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/prices'

    def limit(self, number: int=None) -> PricesLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionPricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPricesLinkagesResponse.parse_obj(json)

    def delete(self, request: SubscriptionPricesLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: SubscriptionPricesLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class PricesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/prices'

    def fields(self, *, subscription_price: Union[SubscriptionPriceField, list[SubscriptionPriceField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None) -> PricesOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_price: the fields to include for returned resources of type subscriptionPrices
        :type subscription_price: Union[SubscriptionPriceField, list[SubscriptionPriceField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionEndpoint
        '''
        if subscription_price: self._set_fields('subscriptionPrices',subscription_price if type(subscription_price) is list else [subscription_price])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'
        SUBSCRIPTION_PRICE_POINT = 'subscriptionPricePoint'

    def filter(self, *, subscription_price_point: Union[str, list[str]]=None, territory: Union[str, list[str]]=None) -> PricesOfSubscriptionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param subscription_price_point: filter by id(s) of related 'subscriptionPricePoint'
        :type subscription_price_point: Union[str, list[str]] = None

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionEndpoint
        '''
        if subscription_price_point: self._set_filter('subscriptionPricePoint', subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PricesOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PricesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPricesResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionPrices
        :rtype: SubscriptionPricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPricesResponse.parse_obj(json)

class PromotedPurchaseLinkageOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/promotedPurchase'

    def get(self) -> SubscriptionPromotedPurchaseLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: SubscriptionPromotedPurchaseLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPromotedPurchaseLinkageResponse.parse_obj(json)

class PromotedPurchaseOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/promotedPurchase'

    def fields(self, *, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None) -> PromotedPurchaseOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchaseOfSubscriptionEndpoint
        '''
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> PromotedPurchaseOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchaseOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> PromotedPurchaseResponse:
        '''Get the resource.

        :returns: Single PromotedPurchase
        :rtype: PromotedPurchaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PromotedPurchaseResponse.parse_obj(json)

class PromotionalOffersLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/promotionalOffers'

    def limit(self, number: int=None) -> PromotionalOffersLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PromotionalOffersLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPromotionalOffersLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionPromotionalOffersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPromotionalOffersLinkagesResponse.parse_obj(json)

class PromotionalOffersOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/promotionalOffers'

    def fields(self, *, subscription_promotional_offer: Union[SubscriptionPromotionalOfferField, list[SubscriptionPromotionalOfferField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None, subscription_promotional_offer_price: Union[SubscriptionPromotionalOfferPriceField, list[SubscriptionPromotionalOfferPriceField]]=None) -> PromotionalOffersOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_promotional_offer: the fields to include for returned resources of type subscriptionPromotionalOffers
        :type subscription_promotional_offer: Union[SubscriptionPromotionalOfferField, list[SubscriptionPromotionalOfferField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :param subscription_promotional_offer_price: the fields to include for returned resources of type subscriptionPromotionalOfferPrices
        :type subscription_promotional_offer_price: Union[SubscriptionPromotionalOfferPriceField, list[SubscriptionPromotionalOfferPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.PromotionalOffersOfSubscriptionEndpoint
        '''
        if subscription_promotional_offer: self._set_fields('subscriptionPromotionalOffers',subscription_promotional_offer if type(subscription_promotional_offer) is list else [subscription_promotional_offer])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        if subscription_promotional_offer_price: self._set_fields('subscriptionPromotionalOfferPrices',subscription_promotional_offer_price if type(subscription_promotional_offer_price) is list else [subscription_promotional_offer_price])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'
        PRICES = 'prices'

    def filter(self, *, territory: Union[str, list[str]]=None) -> PromotionalOffersOfSubscriptionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by territory
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PromotionalOffersOfSubscriptionEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PromotionalOffersOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PromotionalOffersOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, prices: int=None) -> PromotionalOffersOfSubscriptionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.PromotionalOffersOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        return self

    def get(self) -> SubscriptionPromotionalOffersResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionPromotionalOffers
        :rtype: SubscriptionPromotionalOffersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPromotionalOffersResponse.parse_obj(json)

class SubscriptionAvailabilityLinkageOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/subscriptionAvailability'

    def get(self) -> SubscriptionSubscriptionAvailabilityLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: SubscriptionSubscriptionAvailabilityLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionSubscriptionAvailabilityLinkageResponse.parse_obj(json)

class SubscriptionAvailabilityOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/subscriptionAvailability'

    def fields(self, *, subscription_availability: Union[SubscriptionAvailabilityField, list[SubscriptionAvailabilityField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> SubscriptionAvailabilityOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_availability: the fields to include for returned resources of type subscriptionAvailabilities
        :type subscription_availability: Union[SubscriptionAvailabilityField, list[SubscriptionAvailabilityField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAvailabilityOfSubscriptionEndpoint
        '''
        if subscription_availability: self._set_fields('subscriptionAvailabilities',subscription_availability if type(subscription_availability) is list else [subscription_availability])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        AVAILABLE_TERRITORIES = 'availableTerritories'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionAvailabilityOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAvailabilityOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, available_territories: int=None) -> SubscriptionAvailabilityOfSubscriptionEndpoint:
        '''Number of included related resources to return.

        :param available_territories: maximum number of related availableTerritories returned (when they are included). The maximum limit is 50
        :type available_territories: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAvailabilityOfSubscriptionEndpoint
        '''
        if available_territories and available_territories > 50:
            raise ValueError(f'The maximum limit of available_territories is 50')
        if available_territories: self._set_limit(available_territories, 'availableTerritories')

        return self

    def get(self) -> SubscriptionAvailabilityResponse:
        '''Get the resource.

        :returns: Single SubscriptionAvailability
        :rtype: SubscriptionAvailabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionAvailabilityResponse.parse_obj(json)

class SubscriptionLocalizationsLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/subscriptionLocalizations'

    def limit(self, number: int=None) -> SubscriptionLocalizationsLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionLocalizationsLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionSubscriptionLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionSubscriptionLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionSubscriptionLocalizationsLinkagesResponse.parse_obj(json)

class SubscriptionLocalizationsOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/subscriptionLocalizations'

    def fields(self, *, subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None) -> SubscriptionLocalizationsOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param subscription_localization: the fields to include for returned resources of type subscriptionLocalizations
        :type subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionLocalizationsOfSubscriptionEndpoint
        '''
        if subscription_localization: self._set_fields('subscriptionLocalizations',subscription_localization if type(subscription_localization) is list else [subscription_localization])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionLocalizationsOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionLocalizationsOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> SubscriptionLocalizationsOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionLocalizationsOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionLocalizations
        :rtype: SubscriptionLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionLocalizationsResponse.parse_obj(json)

class WinBackOffersLinkagesOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/relationships/winBackOffers'

    def limit(self, number: int=None) -> WinBackOffersLinkagesOfSubscriptionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.WinBackOffersLinkagesOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionWinBackOffersLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionWinBackOffersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionWinBackOffersLinkagesResponse.parse_obj(json)

class WinBackOffersOfSubscriptionEndpoint(IDEndpoint):
    path = '/v1/subscriptions/{id}/winBackOffers'

    def fields(self, *, win_back_offer: Union[WinBackOfferField, list[WinBackOfferField]]=None, win_back_offer_price: Union[WinBackOfferPriceField, list[WinBackOfferPriceField]]=None) -> WinBackOffersOfSubscriptionEndpoint:
        '''Fields to return for included related types.

        :param win_back_offer: the fields to include for returned resources of type winBackOffers
        :type win_back_offer: Union[WinBackOfferField, list[WinBackOfferField]] = None

        :param win_back_offer_price: the fields to include for returned resources of type winBackOfferPrices
        :type win_back_offer_price: Union[WinBackOfferPriceField, list[WinBackOfferPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.WinBackOffersOfSubscriptionEndpoint
        '''
        if win_back_offer: self._set_fields('winBackOffers',win_back_offer if type(win_back_offer) is list else [win_back_offer])
        if win_back_offer_price: self._set_fields('winBackOfferPrices',win_back_offer_price if type(win_back_offer_price) is list else [win_back_offer_price])
        return self
        
    class Include(StringEnum):
        PRICES = 'prices'

    def include(self, relationship: Union[Include, list[Include]]) -> WinBackOffersOfSubscriptionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.WinBackOffersOfSubscriptionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, prices: int=None) -> WinBackOffersOfSubscriptionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.WinBackOffersOfSubscriptionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        return self

    def get(self) -> WinBackOffersResponse:
        '''Get one or more resources.

        :returns: List of WinBackOffers
        :rtype: WinBackOffersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WinBackOffersResponse.parse_obj(json)

