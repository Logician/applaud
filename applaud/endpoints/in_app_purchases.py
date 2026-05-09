from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseEndpoint(IDEndpoint):
    path = '/v1/inAppPurchases/{id}'

    def fields(self, *, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None) -> InAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        return self
        
    class Include(StringEnum):
        APPS = 'apps'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, apps: int=None) -> InAppPurchaseEndpoint:
        '''Number of included related resources to return.

        :param apps: maximum number of related apps returned (when they are included). The maximum limit is 50
        :type apps: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if apps and apps > 50:
            raise ValueError(f'The maximum limit of apps is 50')
        if apps: self._set_limit(apps, 'apps')

        return self

    @deprecated
    def get(self) -> InAppPurchaseResponse:
        '''Get the resource.

        :returns: Single InAppPurchase
        :rtype: InAppPurchaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseResponse.parse_obj(json)

class InAppPurchasesEndpoint(Endpoint):
    path = '/v2/inAppPurchases'

    def create(self, request: InAppPurchaseV2CreateRequest) -> InAppPurchaseV2Response:
        '''Create the resource.

        :param request: InAppPurchase representation
        :type request: InAppPurchaseV2CreateRequest

        :returns: Single InAppPurchase
        :rtype: InAppPurchaseV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseV2Response.parse_obj(json)

class InAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}'

    @endpoint('/v2/inAppPurchases/{id}/appStoreReviewScreenshot')
    def app_store_review_screenshot(self) -> AppStoreReviewScreenshotOfInAppPurchaseEndpoint:
        return AppStoreReviewScreenshotOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/content')
    def content(self) -> ContentOfInAppPurchaseEndpoint:
        return ContentOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/iapPriceSchedule')
    def iap_price_schedule(self) -> IapPriceScheduleOfInAppPurchaseEndpoint:
        return IapPriceScheduleOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/images')
    def images(self) -> ImagesOfInAppPurchaseEndpoint:
        return ImagesOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/inAppPurchaseAvailability')
    def in_app_purchase_availability(self) -> InAppPurchaseAvailabilityOfInAppPurchaseEndpoint:
        return InAppPurchaseAvailabilityOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/inAppPurchaseLocalizations')
    def in_app_purchase_localizations(self) -> InAppPurchaseLocalizationsOfInAppPurchaseEndpoint:
        return InAppPurchaseLocalizationsOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/offerCodes')
    def offer_codes(self) -> OfferCodesOfInAppPurchaseEndpoint:
        return OfferCodesOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/pricePoints')
    def price_points(self) -> PricePointsOfInAppPurchaseEndpoint:
        return PricePointsOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/promotedPurchase')
    def promoted_purchase(self) -> PromotedPurchaseOfInAppPurchaseEndpoint:
        return PromotedPurchaseOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/appStoreReviewScreenshot')
    def app_store_review_screenshot_linkage(self) -> AppStoreReviewScreenshotLinkageOfInAppPurchaseEndpoint:
        return AppStoreReviewScreenshotLinkageOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/content')
    def content_linkage(self) -> ContentLinkageOfInAppPurchaseEndpoint:
        return ContentLinkageOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/iapPriceSchedule')
    def iap_price_schedule_linkage(self) -> IapPriceScheduleLinkageOfInAppPurchaseEndpoint:
        return IapPriceScheduleLinkageOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/images')
    def images_linkages(self) -> ImagesLinkagesOfInAppPurchaseEndpoint:
        return ImagesLinkagesOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/inAppPurchaseAvailability')
    def in_app_purchase_availability_linkage(self) -> InAppPurchaseAvailabilityLinkageOfInAppPurchaseEndpoint:
        return InAppPurchaseAvailabilityLinkageOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/inAppPurchaseLocalizations')
    def in_app_purchase_localizations_linkages(self) -> InAppPurchaseLocalizationsLinkagesOfInAppPurchaseEndpoint:
        return InAppPurchaseLocalizationsLinkagesOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/offerCodes')
    def offer_codes_linkages(self) -> OfferCodesLinkagesOfInAppPurchaseEndpoint:
        return OfferCodesLinkagesOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/pricePoints')
    def price_points_linkages(self) -> PricePointsLinkagesOfInAppPurchaseEndpoint:
        return PricePointsLinkagesOfInAppPurchaseEndpoint(self.id, self.session)
        
    @endpoint('/v2/inAppPurchases/{id}/relationships/promotedPurchase')
    def promoted_purchase_linkage(self) -> PromotedPurchaseLinkageOfInAppPurchaseEndpoint:
        return PromotedPurchaseLinkageOfInAppPurchaseEndpoint(self.id, self.session)
        
    def fields(self, *, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]]=None, in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]]=None, in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]]=None, in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]]=None, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]]=None, in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]]=None, in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]]=None, in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]]=None) -> InAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param in_app_purchase_localization: the fields to include for returned resources of type inAppPurchaseLocalizations
        :type in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]] = None

        :param in_app_purchase_price_point: the fields to include for returned resources of type inAppPurchasePricePoints
        :type in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]] = None

        :param in_app_purchase_content: the fields to include for returned resources of type inAppPurchaseContents
        :type in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]] = None

        :param in_app_purchase_app_store_review_screenshot: the fields to include for returned resources of type inAppPurchaseAppStoreReviewScreenshots
        :type in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]] = None

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :param in_app_purchase_price_schedule: the fields to include for returned resources of type inAppPurchasePriceSchedules
        :type in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]] = None

        :param in_app_purchase_availability: the fields to include for returned resources of type inAppPurchaseAvailabilities
        :type in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]] = None

        :param in_app_purchase_image: the fields to include for returned resources of type inAppPurchaseImages
        :type in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]] = None

        :param in_app_purchase_offer_code: the fields to include for returned resources of type inAppPurchaseOfferCodes
        :type in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if in_app_purchase_localization: self._set_fields('inAppPurchaseLocalizations',in_app_purchase_localization if type(in_app_purchase_localization) is list else [in_app_purchase_localization])
        if in_app_purchase_price_point: self._set_fields('inAppPurchasePricePoints',in_app_purchase_price_point if type(in_app_purchase_price_point) is list else [in_app_purchase_price_point])
        if in_app_purchase_content: self._set_fields('inAppPurchaseContents',in_app_purchase_content if type(in_app_purchase_content) is list else [in_app_purchase_content])
        if in_app_purchase_app_store_review_screenshot: self._set_fields('inAppPurchaseAppStoreReviewScreenshots',in_app_purchase_app_store_review_screenshot if type(in_app_purchase_app_store_review_screenshot) is list else [in_app_purchase_app_store_review_screenshot])
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        if in_app_purchase_price_schedule: self._set_fields('inAppPurchasePriceSchedules',in_app_purchase_price_schedule if type(in_app_purchase_price_schedule) is list else [in_app_purchase_price_schedule])
        if in_app_purchase_availability: self._set_fields('inAppPurchaseAvailabilities',in_app_purchase_availability if type(in_app_purchase_availability) is list else [in_app_purchase_availability])
        if in_app_purchase_image: self._set_fields('inAppPurchaseImages',in_app_purchase_image if type(in_app_purchase_image) is list else [in_app_purchase_image])
        if in_app_purchase_offer_code: self._set_fields('inAppPurchaseOfferCodes',in_app_purchase_offer_code if type(in_app_purchase_offer_code) is list else [in_app_purchase_offer_code])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_LOCALIZATIONS = 'inAppPurchaseLocalizations'
        PRICE_POINTS = 'pricePoints'
        CONTENT = 'content'
        APP_STORE_REVIEW_SCREENSHOT = 'appStoreReviewScreenshot'
        PROMOTED_PURCHASE = 'promotedPurchase'
        IAP_PRICE_SCHEDULE = 'iapPriceSchedule'
        IN_APP_PURCHASE_AVAILABILITY = 'inAppPurchaseAvailability'
        IMAGES = 'images'
        OFFER_CODES = 'offerCodes'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, images: int=None, in_app_purchase_localizations: int=None, offer_codes: int=None, price_points: int=None) -> InAppPurchaseEndpoint:
        '''Number of included related resources to return.

        :param images: maximum number of related images returned (when they are included). The maximum limit is 50
        :type images: int = None

        :param in_app_purchase_localizations: maximum number of related inAppPurchaseLocalizations returned (when they are included). The maximum limit is 50
        :type in_app_purchase_localizations: int = None

        :param offer_codes: maximum number of related offerCodes returned (when they are included). The maximum limit is 50
        :type offer_codes: int = None

        :param price_points: maximum number of related pricePoints returned (when they are included). The maximum limit is 8000
        :type price_points: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if images and images > 50:
            raise ValueError(f'The maximum limit of images is 50')
        if images: self._set_limit(images, 'images')

        if in_app_purchase_localizations and in_app_purchase_localizations > 50:
            raise ValueError(f'The maximum limit of in_app_purchase_localizations is 50')
        if in_app_purchase_localizations: self._set_limit(in_app_purchase_localizations, 'inAppPurchaseLocalizations')

        if offer_codes and offer_codes > 50:
            raise ValueError(f'The maximum limit of offer_codes is 50')
        if offer_codes: self._set_limit(offer_codes, 'offerCodes')

        if price_points and price_points > 8000:
            raise ValueError(f'The maximum limit of price_points is 8000')
        if price_points: self._set_limit(price_points, 'pricePoints')

        return self

    def get(self) -> InAppPurchaseV2Response:
        '''Get the resource.

        :returns: Single InAppPurchase
        :rtype: InAppPurchaseV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2Response.parse_obj(json)

    def update(self, request: InAppPurchaseV2UpdateRequest) -> InAppPurchaseV2Response:
        '''Modify the resource.

        :param request: InAppPurchase representation
        :type request: InAppPurchaseV2UpdateRequest

        :returns: Single InAppPurchase
        :rtype: InAppPurchaseV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return InAppPurchaseV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppStoreReviewScreenshotLinkageOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/appStoreReviewScreenshot'

    def get(self) -> InAppPurchaseV2AppStoreReviewScreenshotLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: InAppPurchaseV2AppStoreReviewScreenshotLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2AppStoreReviewScreenshotLinkageResponse.parse_obj(json)

class AppStoreReviewScreenshotOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/appStoreReviewScreenshot'

    def fields(self, *, in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None) -> AppStoreReviewScreenshotOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_app_store_review_screenshot: the fields to include for returned resources of type inAppPurchaseAppStoreReviewScreenshots
        :type in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewScreenshotOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_app_store_review_screenshot: self._set_fields('inAppPurchaseAppStoreReviewScreenshots',in_app_purchase_app_store_review_screenshot if type(in_app_purchase_app_store_review_screenshot) is list else [in_app_purchase_app_store_review_screenshot])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreReviewScreenshotOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewScreenshotOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseAppStoreReviewScreenshotResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseAppStoreReviewScreenshot
        :rtype: InAppPurchaseAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseAppStoreReviewScreenshotResponse.parse_obj(json)

class ContentLinkageOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/content'

    def get(self) -> InAppPurchaseV2ContentLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: InAppPurchaseV2ContentLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2ContentLinkageResponse.parse_obj(json)

class ContentOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/content'

    def fields(self, *, in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None) -> ContentOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_content: the fields to include for returned resources of type inAppPurchaseContents
        :type in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.ContentOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_content: self._set_fields('inAppPurchaseContents',in_app_purchase_content if type(in_app_purchase_content) is list else [in_app_purchase_content])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'

    def include(self, relationship: Union[Include, list[Include]]) -> ContentOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ContentOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseContentResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseContent
        :rtype: InAppPurchaseContentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseContentResponse.parse_obj(json)

class IapPriceScheduleLinkageOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/iapPriceSchedule'

    def get(self) -> InAppPurchaseV2IapPriceScheduleLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: InAppPurchaseV2IapPriceScheduleLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2IapPriceScheduleLinkageResponse.parse_obj(json)

class IapPriceScheduleOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/iapPriceSchedule'

    def fields(self, *, in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]]=None) -> IapPriceScheduleOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_price_schedule: the fields to include for returned resources of type inAppPurchasePriceSchedules
        :type in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param in_app_purchase_price: the fields to include for returned resources of type inAppPurchasePrices
        :type in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.IapPriceScheduleOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_price_schedule: self._set_fields('inAppPurchasePriceSchedules',in_app_purchase_price_schedule if type(in_app_purchase_price_schedule) is list else [in_app_purchase_price_schedule])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if in_app_purchase_price: self._set_fields('inAppPurchasePrices',in_app_purchase_price if type(in_app_purchase_price) is list else [in_app_purchase_price])
        return self
        
    class Include(StringEnum):
        BASE_TERRITORY = 'baseTerritory'
        MANUAL_PRICES = 'manualPrices'
        AUTOMATIC_PRICES = 'automaticPrices'

    def include(self, relationship: Union[Include, list[Include]]) -> IapPriceScheduleOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.IapPriceScheduleOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, manual_prices: int=None, automatic_prices: int=None) -> IapPriceScheduleOfInAppPurchaseEndpoint:
        '''Number of included related resources to return.

        :param manual_prices: maximum number of related manualPrices returned (when they are included). The maximum limit is 50
        :type manual_prices: int = None

        :param automatic_prices: maximum number of related automaticPrices returned (when they are included). The maximum limit is 50
        :type automatic_prices: int = None

        :returns: self
        :rtype: applaud.endpoints.IapPriceScheduleOfInAppPurchaseEndpoint
        '''
        if manual_prices and manual_prices > 50:
            raise ValueError(f'The maximum limit of manual_prices is 50')
        if manual_prices: self._set_limit(manual_prices, 'manualPrices')

        if automatic_prices and automatic_prices > 50:
            raise ValueError(f'The maximum limit of automatic_prices is 50')
        if automatic_prices: self._set_limit(automatic_prices, 'automaticPrices')

        return self

    def get(self) -> InAppPurchasePriceScheduleResponse:
        '''Get the resource.

        :returns: Single InAppPurchasePriceSchedule
        :rtype: InAppPurchasePriceScheduleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePriceScheduleResponse.parse_obj(json)

class ImagesLinkagesOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/images'

    def limit(self, number: int=None) -> ImagesLinkagesOfInAppPurchaseEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ImagesLinkagesOfInAppPurchaseEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseV2ImagesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseV2ImagesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2ImagesLinkagesResponse.parse_obj(json)

class ImagesOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/images'

    def fields(self, *, in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None) -> ImagesOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_image: the fields to include for returned resources of type inAppPurchaseImages
        :type in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.ImagesOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_image: self._set_fields('inAppPurchaseImages',in_app_purchase_image if type(in_app_purchase_image) is list else [in_app_purchase_image])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE = 'inAppPurchase'

    def include(self, relationship: Union[Include, list[Include]]) -> ImagesOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ImagesOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ImagesOfInAppPurchaseEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ImagesOfInAppPurchaseEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseImagesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchaseImages
        :rtype: InAppPurchaseImagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseImagesResponse.parse_obj(json)

class InAppPurchaseAvailabilityLinkageOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/inAppPurchaseAvailability'

    def get(self) -> InAppPurchaseV2InAppPurchaseAvailabilityLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: InAppPurchaseV2InAppPurchaseAvailabilityLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2InAppPurchaseAvailabilityLinkageResponse.parse_obj(json)

class InAppPurchaseAvailabilityOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/inAppPurchaseAvailability'

    def fields(self, *, in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> InAppPurchaseAvailabilityOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_availability: the fields to include for returned resources of type inAppPurchaseAvailabilities
        :type in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAvailabilityOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_availability: self._set_fields('inAppPurchaseAvailabilities',in_app_purchase_availability if type(in_app_purchase_availability) is list else [in_app_purchase_availability])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        AVAILABLE_TERRITORIES = 'availableTerritories'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseAvailabilityOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAvailabilityOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, available_territories: int=None) -> InAppPurchaseAvailabilityOfInAppPurchaseEndpoint:
        '''Number of included related resources to return.

        :param available_territories: maximum number of related availableTerritories returned (when they are included). The maximum limit is 50
        :type available_territories: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAvailabilityOfInAppPurchaseEndpoint
        '''
        if available_territories and available_territories > 50:
            raise ValueError(f'The maximum limit of available_territories is 50')
        if available_territories: self._set_limit(available_territories, 'availableTerritories')

        return self

    def get(self) -> InAppPurchaseAvailabilityResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseAvailability
        :rtype: InAppPurchaseAvailabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseAvailabilityResponse.parse_obj(json)

class InAppPurchaseLocalizationsLinkagesOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/inAppPurchaseLocalizations'

    def limit(self, number: int=None) -> InAppPurchaseLocalizationsLinkagesOfInAppPurchaseEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseLocalizationsLinkagesOfInAppPurchaseEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseV2InAppPurchaseLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseV2InAppPurchaseLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2InAppPurchaseLocalizationsLinkagesResponse.parse_obj(json)

class InAppPurchaseLocalizationsOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/inAppPurchaseLocalizations'

    def fields(self, *, in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None) -> InAppPurchaseLocalizationsOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_localization: the fields to include for returned resources of type inAppPurchaseLocalizations
        :type in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseLocalizationsOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_localization: self._set_fields('inAppPurchaseLocalizations',in_app_purchase_localization if type(in_app_purchase_localization) is list else [in_app_purchase_localization])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseLocalizationsOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseLocalizationsOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> InAppPurchaseLocalizationsOfInAppPurchaseEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseLocalizationsOfInAppPurchaseEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchaseLocalizations
        :rtype: InAppPurchaseLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseLocalizationsResponse.parse_obj(json)

class OfferCodesLinkagesOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/offerCodes'

    def limit(self, number: int=None) -> OfferCodesLinkagesOfInAppPurchaseEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.OfferCodesLinkagesOfInAppPurchaseEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseV2OfferCodesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseV2OfferCodesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2OfferCodesLinkagesResponse.parse_obj(json)

class OfferCodesOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/offerCodes'

    def fields(self, *, in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]]=None, in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]]=None, in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]]=None, in_app_purchase_offer_price: Union[InAppPurchaseOfferPriceField, list[InAppPurchaseOfferPriceField]]=None) -> OfferCodesOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_offer_code: the fields to include for returned resources of type inAppPurchaseOfferCodes
        :type in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]] = None

        :param in_app_purchase_offer_code_one_time_use_code: the fields to include for returned resources of type inAppPurchaseOfferCodeOneTimeUseCodes
        :type in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]] = None

        :param in_app_purchase_offer_code_custom_code: the fields to include for returned resources of type inAppPurchaseOfferCodeCustomCodes
        :type in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]] = None

        :param in_app_purchase_offer_price: the fields to include for returned resources of type inAppPurchaseOfferPrices
        :type in_app_purchase_offer_price: Union[InAppPurchaseOfferPriceField, list[InAppPurchaseOfferPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.OfferCodesOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_offer_code: self._set_fields('inAppPurchaseOfferCodes',in_app_purchase_offer_code if type(in_app_purchase_offer_code) is list else [in_app_purchase_offer_code])
        if in_app_purchase_offer_code_one_time_use_code: self._set_fields('inAppPurchaseOfferCodeOneTimeUseCodes',in_app_purchase_offer_code_one_time_use_code if type(in_app_purchase_offer_code_one_time_use_code) is list else [in_app_purchase_offer_code_one_time_use_code])
        if in_app_purchase_offer_code_custom_code: self._set_fields('inAppPurchaseOfferCodeCustomCodes',in_app_purchase_offer_code_custom_code if type(in_app_purchase_offer_code_custom_code) is list else [in_app_purchase_offer_code_custom_code])
        if in_app_purchase_offer_price: self._set_fields('inAppPurchaseOfferPrices',in_app_purchase_offer_price if type(in_app_purchase_offer_price) is list else [in_app_purchase_offer_price])
        return self
        
    class Include(StringEnum):
        ONE_TIME_USE_CODES = 'oneTimeUseCodes'
        CUSTOM_CODES = 'customCodes'
        PRICES = 'prices'

    def filter(self, *, territory: Union[str, list[str]]=None) -> OfferCodesOfInAppPurchaseEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by territory
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.OfferCodesOfInAppPurchaseEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> OfferCodesOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.OfferCodesOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, one_time_use_codes: int=None, custom_codes: int=None, prices: int=None) -> OfferCodesOfInAppPurchaseEndpoint:
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
        :rtype: applaud.endpoints.OfferCodesOfInAppPurchaseEndpoint
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

    def get(self) -> InAppPurchaseOfferCodesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchaseOfferCodes
        :rtype: InAppPurchaseOfferCodesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodesResponse.parse_obj(json)

class PricePointsLinkagesOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/pricePoints'

    def limit(self, number: int=None) -> PricePointsLinkagesOfInAppPurchaseEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsLinkagesOfInAppPurchaseEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseV2PricePointsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseV2PricePointsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2PricePointsLinkagesResponse.parse_obj(json)

class PricePointsOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/pricePoints'

    def fields(self, *, in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> PricePointsOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_price_point: the fields to include for returned resources of type inAppPurchasePricePoints
        :type in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfInAppPurchaseEndpoint
        '''
        if in_app_purchase_price_point: self._set_fields('inAppPurchasePricePoints',in_app_purchase_price_point if type(in_app_purchase_price_point) is list else [in_app_purchase_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None) -> PricePointsOfInAppPurchaseEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfInAppPurchaseEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PricePointsOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfInAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PricePointsOfInAppPurchaseEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfInAppPurchaseEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchasePricePointsResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchasePricePoints
        :rtype: InAppPurchasePricePointsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePricePointsResponse.parse_obj(json)

class PromotedPurchaseLinkageOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/relationships/promotedPurchase'

    def get(self) -> InAppPurchaseV2PromotedPurchaseLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: InAppPurchaseV2PromotedPurchaseLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseV2PromotedPurchaseLinkageResponse.parse_obj(json)

class PromotedPurchaseOfInAppPurchaseEndpoint(IDEndpoint):
    path = '/v2/inAppPurchases/{id}/promotedPurchase'

    def fields(self, *, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None) -> PromotedPurchaseOfInAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchaseOfInAppPurchaseEndpoint
        '''
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> PromotedPurchaseOfInAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchaseOfInAppPurchaseEndpoint
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

