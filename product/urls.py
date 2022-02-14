from django.urls import path
from .views import  AllProductList,SearchView,MainPictureExportalCreateView, InternalProductPanelList, \
    InternalProductDetail, PartialPictureExportalCreateView ,InternalProductCreateView, ExportalProductPanelList, \
    ExportalProductListView, ExportalProductDetail, ExportalProductCreateView, \
    LinedProductList, LinedProductPanelList, LinedProductDetail, LinedProductCreateView, \
    RejectedProductList, RejectedProductCreateView, LoadedProductList, LoadedProductCreateView, \
    InternalImage, ExportalImage, SpecialOfferList, ProductionReportsList, LoadedReports, DomesticInventory, \
    ExportalInventory,AllProductListComplete,SpecialOfferListComplete,ExportalProductListCompleteView

app_name = "product"
urlpatterns = [
    path("exportal_logo/",MainPictureExportalCreateView,name="exportal_logo"),
    path("PartialPictureExportalCreateView/",PartialPictureExportalCreateView,name="partial_pic_create"),
    path("search/",SearchView, name="search"),
    path("exportal_product_complete/",ExportalProductListCompleteView.as_view(), name="exportal_product_Complete"),
    path("special_product_complete/",SpecialOfferListComplete.as_view(), name="special_product_Complete"),
    path("all_product_complete/", AllProductListComplete.as_view(), name="all_product_Complete"),
    path("all_product/", AllProductList.as_view(), name="all_product"),
    path("Interna_list/", InternalProductPanelList.as_view(), name="internal_list_panel"),
    path("internal_product_detail/<int:pk>/", InternalProductDetail.as_view(), name="internal_product_detail"),
    path("internal_product_create/", InternalProductCreateView.as_view(), name="internal_product_create"),
    path("internal_image/", InternalImage.as_view(), name="internal_image"),
    path("exportal_list/", ExportalProductListView.as_view(), name="exportal_list"),
    path("exportal_list_panel/", ExportalProductPanelList.as_view(), name="exportal_list_panel"),
    path("exportal_product_detail/<int:pk>/", ExportalProductDetail.as_view(), name="exportal_product_detail"),
    path("exportal_product_create/", ExportalProductCreateView.as_view(), name="exportal_product_create"),
    path("exportal_image/", ExportalImage.as_view(), name="exportal_image"),
    path("lined_product/", LinedProductList.as_view(), name="lined_product"),
    path("lined_product_panel/", LinedProductPanelList.as_view(), name="lined_product_panel"),
    path("lined_product_detail/<int:unuqe_id>/", LinedProductDetail.as_view(), name="lined_product_detail"),
    path("lined_product_create/", LinedProductCreateView.as_view(), name="lined_product_create"),
    path("rejected_product/", RejectedProductList.as_view(), name="rejected_product"),
    path("rejected_product_uploade/", RejectedProductCreateView, name="rejected_product_update"),
    path("Loaded_product/", LoadedProductList.as_view(), name="loaded_product"),
    path("Loaded_product_uploade/", LoadedProductCreateView.as_view(), name="loaded_product_update"),
    path("special_offer/", SpecialOfferList.as_view(), name="special_offer"),
    path("production_reportes/", ProductionReportsList.as_view(), name="production_reports"),
    path("loaded_reportes/", LoadedReports.as_view(), name="loaded_reports"),
    path("domestic_reports/", DomesticInventory.as_view(), name="internal_reports"),
    path("exportal_reports/", ExportalInventory.as_view(), name="exportal_reports"),
]
