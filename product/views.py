from django.shortcuts import render, redirect
from tablib import Dataset
from .filters import ProductFilter, LoadedFilter, DomesticFilter, ExportalFilter
from django.views.generic import ListView, View, DetailView
from .models import ExportalProduct, InternalProduct, LinedProduct, ProductBase, Rejected, Loaded, Internal_Image, \
    Exportal_Image
from django.contrib.auth.mixins import LoginRequiredMixin
from .resources import Internal_Product_Resource, Exportal_Product_Resource, Internal_Product_Image_Resource, \
    Exportal_Product_Image_Resource, Lined_Product_Resource, Loaded_Product_Resource
from django.db.models import Sum
import random
from django.db.models import Q

# Create your views here.

class SpecialOfferList(View):
    def get(self, request):
        special_internal = InternalProduct.objects.filter(is_special=True)[:10]
        special_exportal = ExportalProduct.objects.filter(is_special=True)[:10]
        return render(request, "product/special_offer_list.html",
                      {"exportal_list": special_exportal, "special_internal": special_internal})


class SpecialOfferListComplete(View):
    def get(self, request):
        special_internal = InternalProduct.objects.filter(is_special=True)[:10]
        special_exportal = ExportalProduct.objects.filter(is_special=True)[:10]
        return render(request, "product/special_offer_complete_list.html",
                      {"exportal_list": special_exportal, "special_internal": special_internal})    
    
    
    
# class HomePage(LoginRequiredMixin, View):
#     def get(self, request):
#         context = {
#             "exportal": ExportalProduct.objects.all()[:3],
#             "lined": LinedProduct.objects.all()[:3],
#             "special_offer": ProductBase.objects.filter(is_special=True)[:3]
#         }
#         return render(request, "product/", context)


class AllProductList(LoginRequiredMixin, View):
    def get(self, request):
        base_count = ProductBase.objects.all().count()
        lined_count = LinedProduct.objects.all().count()
        total_count = base_count + lined_count
        total_ton = ProductBase.objects.aggregate(Sum("approximate_tonnage"))['approximate_tonnage__sum']
        # stone_name = request.GET.get("stone_name")
        # stone_type = request.GET.get("stone_type")
        # color = request.GET.get("color")
        # mine = request.GET.get("mine")
        # grade = request.GET.get("grade")
        # if stone_name or stone_type or color or mine or grade:
        #     internal = InternalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade)
        #     exportal = ExportalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade, color_code=color)
        context = {
            "internal": InternalProduct.objects.all()[:10],
            "exportal": ExportalProduct.objects.all()[:10],
            "lined": LinedProduct.objects.all(),
            "total_count": total_count,
            "total_ton": total_ton
        }
        return render(request, "product/all_product.html", context)

class AllProductListComplete(LoginRequiredMixin, View):
    def get(self, request):
        base_count = ProductBase.objects.all().count()
        lined_count = LinedProduct.objects.all().count()
        total_count = base_count + lined_count
        total_ton = ProductBase.objects.aggregate(Sum("approximate_tonnage"))['approximate_tonnage__sum']
        # stone_name = request.GET.get("stone_name")
        # stone_type = request.GET.get("stone_type")
        # color = request.GET.get("color")
        # mine = request.GET.get("mine")
        # grade = request.GET.get("grade")
        # if stone_name or stone_type or color or mine or grade:
        #     internal = InternalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade)
        #     exportal = ExportalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade, color_code=color)
        context = {
            "internal": InternalProduct.objects.all(),
            "exportal": ExportalProduct.objects.all(),
            "lined": LinedProduct.objects.all(),
            "total_count": total_count,
            "total_ton": total_ton
        }
        return render(request, "product/all_product_complete.html", context)    
    
    

# INTERNAL PRODUCT
class InternalProductPanelList(ListView):
    model = InternalProduct
    template_name = "product/internal_list_panel.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(InternalProductPanelList, self).get_context_data(*args, **kwargs)
        context_data["total"] = InternalProduct.objects.all().count()
        context_data["tonajze"] = InternalProduct.objects.all().aggregate(Sum("approximate_tonnage"))['approximate_tonnage__sum']
        return context_data


class InternalProductDetail(DetailView):
    model = InternalProduct
    slug_field = "pk"
    slug_url_kwarg = "pk"
    template_name = "product/internal_detail.html"


class InternalProductCreateView(View):

    def get(self, request):
        return render(request, "product/add_internal.html")

    def post(request):
        internal_resource = Internal_Product_Resource()
        dataset = Dataset()
        new_internal = request.FILES['file']
        imported_data = dataset.load(new_internal.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = InternalProduct(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
            )
            value.save()
        return render(request, "product/add_internal.html")


class InternalImage(View):

    def post(request):
        internal_image_resource = Internal_Product_Image_Resource()
        dataset = Dataset()
        new_internal_image = request.FILES['file']
        imported_data = dataset.load(new_internal_image.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Internal_Image(
                data[0],
                data[1],
            )
            value.save()
        return redirect("config:panel_home")


# Exportal
class ExportalProductPanelList(LoginRequiredMixin, ListView):
    model = ExportalProduct
    template_name = "product/exportal_list_panel.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(ExportalProductPanelList, self).get_context_data(*args, **kwargs)
        context_data["total"] = ExportalProduct.objects.all().count()
        context_data["tonajze"] = ExportalProduct.objects.aggregate(Sum("approximate_tonnage"))['approximate_tonnage__sum']
        return context_data


class ExportalProductListView(LoginRequiredMixin, ListView):
    model = ExportalProduct
    template_name = "product/exportal_list.html"

class ExportalProductListCompleteView(LoginRequiredMixin, ListView):
    model = ExportalProduct
    template_name = "product/exportal_list_complete.html"    
    
    

class ExportalProductDetail(DetailView):
    model = ExportalProduct
    slug_field = "pk"
    slug_url_kwarg = "pk"
    template_name = "product/exportal_detail.html"


class ExportalProductCreateView(View):

    def get(self, request):
        return render(request, "product/add_exportal.html")

    def post(self, request):
        internal_resource = Exportal_Product_Resource()
        dataset = Dataset()
        new_exportal = request.FILES['file']
        imported_data = dataset.load(new_exportal.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = ExportalProduct(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
            )
            value.save()
        return render(request, "product/add_exportal.html")


class ExportalImage(View):

    def post(self, request):
        exportal_resource = Exportal_Product_Image_Resource()
        dataset = Dataset()
        new_exportal_image = request.FILES['file']
        imported_data = dataset.load(new_exportal_image.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Exportal_Image(
                data[0],
                data[1],
            )
            value.save()
        return redirect("config:panel_home")


# Lined
class LinedProductList(ListView):
    model = LinedProduct
    template_name = "product/"


class LinedProductPanelList(ListView):
    model = LinedProduct
    template_name = "product/line_list.html"


class LinedProductDetail(DetailView):
    model = InternalProduct
    slug_field = "uniqe_id"
    slug_url_kwarg = "uniqe_id"
    template_name = "product/line_list.html"


class LinedProductCreateView(View):

    def get(self, request):
        return render(request, "product/")

    def post(request):
        lined_resource = Lined_Product_Resource()
        dataset = Dataset()
        new_lined = request.FILES['file']
        imported_data = dataset.load(new_lined.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = LinedProduct(
                data[0],
            )
            value.save()
        return render(request, "")


# REJECTED

class RejectedProductList(ListView):
    model = Rejected
    template_name = "product/rejected_list.html"


class RejectedProductCreateView(View):

    def post(self, request):
        lined_resource = Lined_Product_Resource()
        dataset = Dataset()
        new_lined = request.FILES['file']
        imported_data = dataset.load(new_lined.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Rejected(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6]
            )
            value.save()
        return redirect("config:panel_home")


# Loaded


class LoadedProductList(ListView):
    model = Loaded
    template_name = "product/loaded_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(LoadedProductList, self).get_context_data(*args, **kwargs)
        # context_data["total"]=Loaded.objects.all().count()
        # context_data["tonajze"]=Loaded.objects.aggregate(Sum("weight_of_scales"))
        return context_data


class LoadedProductCreateView(View):

    def post(self, request):
        loaded_resource = Loaded_Product_Resource()
        dataset = Dataset()
        new_loaded = request.FILES['myfile']
        imported_data = dataset.load(new_loaded.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Loaded(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
            )
            value.save()
        return redirect("config:panel_home")


class ProductionReportsList(View):
    def get(self, request):
        queryset = ProductFilter(request.GET, queryset=ProductBase.objects.all())
        return render(request, 'product/production_reports.html', {'filter': queryset})


class LoadedReports(View):
    def get(self, request):
        queryset = LoadedFilter(request.GET, queryset=Loaded.objects.all())
        return render(request, 'product/loaded_reports.html', {'filter': queryset})


class DomesticInventory(View):
    def get(self, request):
        queryset = DomesticFilter(request.GET, queryset=InternalProduct.objects.all())
        return render(request, 'product/internal_reports.html', {'filter': queryset})


class ExportalInventory(View):
    def get(self, request):
        queryset = ExportalFilter(request.GET, queryset=ExportalProduct.objects.all())
        return render(request, 'product/exportal_reports.html', {'filter': queryset})

class SearchView(View):
    def get(self, request):
        internal_product = InternalProduct.objects.filter(
            Q(mine__stone_type=request.GET.get("stone_type")) | Q(stone_name=request.GET.get("stone_name")),
            Q(mine__name=request.GET.get("mine")) | Q(grading_code=request.GET.get("grading_code"))| Q(length_lt=request.GET.get("length")),
            Q(height_lt=request.GET.get("height")) | Q(width_lt=request.GET.get("width")) )
        exportal_product = ExportalProduct.objects.filter(
            Q(mine__stone_type=request.GET.get("stone_type")) | Q(stone_name=request.GET.get("stone_name")),
            Q(mine__name=request.GET.get("mine")) | Q(grading_code=request.GET.get("grading_code")),
            Q(color_code=request.GET.get("color_code")) | Q(length_lt=request.GET.get("length")),
            Q(height_lt=request.GET.get("height")) | Q(width_lt=request.GET.get("width"))
        )
        return render(request, "product/search.html", {"internal": internal_product, "exportal": exportal_product})    
    
    