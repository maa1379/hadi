from django.urls import path
from .views import AllProductList, SearchView, MainPictureExportalCreateView, InternalProductPanelList, \
    PartialPictureExportalCreateView, InternalProductCreateView, ExportalProductPanelList, \
    ExportalProductListView, ExportalProductCreateView, \
    LinedProductList, LinedProductPanelList, LinedProductCreateView, \
    RejectedProductList, LoadedProductList, LoadedProductCreateView, \
    InternalImage, ExportalImage, SpecialOfferList, ProductionReportsList, LoadedReports, DomesticInventory, \
    ExportalInventory, AllProductListComplete, SpecialOfferListComplete, ExportalProductListCompleteView, \
    lined_product_image, PartialPictureInternalCreateView, rejected_update, rejected_upload, \
    product_detail

app_name = "product"
urlpatterns = [
    path("exportal_logo/",MainPictureExportalCreateView,name="exportal_logo"),
    path("lined_product_images/",lined_product_image,name="lined_product_image"),
    path("PartialPictureExportalCreateView/",PartialPictureExportalCreateView,name="partial_pic_create"),
    path("search/",SearchView, name="search"),
    path("exportal_product_complete/",ExportalProductListCompleteView.as_view(), name="exportal_product_Complete"),
    path("special_product_complete/",SpecialOfferListComplete.as_view(), name="special_product_Complete"),
    path("all_product_complete/", AllProductListComplete.as_view(), name="all_product_Complete"),
    path("all_product/", AllProductList.as_view(), name="all_product"),
    path("Interna_list/", InternalProductPanelList.as_view(), name="internal_list_panel"),
    path("internal_product_detail/<str:unique_id>/", product_detail, name="internal_product_detail"),
    path("exportal_product_detail/<str:unique_id>/", product_detail, name="exportal_product_detail"),
    path("lined_product_detail/<str:unique_id>/", product_detail, name="lined_product_detail"),
    path("internal_image/", InternalImage, name="internal_image"),
    path("exportal_list/", ExportalProductListView.as_view(), name="exportal_list"),
    path("exportal_list_panel/", ExportalProductPanelList.as_view(), name="exportal_list_panel"),
    path("internal_product_create/", InternalProductCreateView.as_view(), name="internal_product_create"),
    path("exportal_product_create/", ExportalProductCreateView.as_view(), name="exportal_product_create"),
    path("exportal_image/", ExportalImage.as_view(), name="exportal_image"),
    path("internal_image_gallery/", PartialPictureInternalCreateView, name="internal_image_gallery"),
    path("lined_product/", LinedProductList.as_view(), name="lined_product"),
    path("lined_product_panel/", LinedProductPanelList.as_view(), name="lined_product_panel"),
    path("lined_product_create/", LinedProductCreateView.as_view(), name="lined_product_create"),
    path("rejected_product/", RejectedProductList.as_view(), name="rejected_product"),
    path("Loaded_product/", LoadedProductList.as_view(), name="loaded_product"),
    path("Loaded_product_uploade/", LoadedProductCreateView, name="loaded_product_update"),
    path("rejected_update/", rejected_update, name="rejected_update"),
    path("rejected_upload/", rejected_upload, name="rejected_upload"),
    path("special_offer/", SpecialOfferList.as_view(), name="special_offer"),
    path("production_reportes/", ProductionReportsList.as_view(), name="production_reports"),
    path("loaded_reportes/", LoadedReports.as_view(), name="loaded_reports"),
    path("domestic_reports/", DomesticInventory.as_view(), name="internal_reports"),
    path("exportal_reports/", ExportalInventory.as_view(), name="exportal_reports"),
]
