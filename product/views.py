from django.shortcuts import render, redirect, get_object_or_404
from tablib import Dataset

from account.models import User
from demand.models import HoldForm, SampleForm, VisitForm, Hold, Visit, Sample
from .filters import ProductFilter, LoadedFilter, DomesticFilter, ExportalFilter, RejectedFilter
from django.views.generic import ListView, View, DetailView
from .models import ExportalProduct, InternalProduct, LinedProduct, ProductBase, Rejected, Loaded, Internal_Image, \
    Exportal_Image, ExportalLogo, ExportalFileLogo, InternalFileLogo, linedFile, ImageExportalModel, ExportalFile, \
    InternalFile

from django.contrib.auth.mixins import LoginRequiredMixin
from .resources import Internal_Product_Resource, Exportal_Product_Resource, Internal_Product_Image_Resource, \
    Exportal_Product_Image_Resource, Lined_Product_Resource, Loaded_Product_Resource, Rejected_Product_Resource
from django.db.models import Sum
import random
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from zipfile import ZipFile
import os
from pathlib import Path
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from .forms import ExportalFileForm, ExportalFileLogoForm, InternalFileLogoForm, linedFileForm, InternalFileForm


# Create your views here.

class SpecialOfferList(View):
    def get(self, request):
        special_internal = InternalProduct.objects.filter(is_special=True, active=True)[:10]
        special_exportal = ExportalProduct.objects.filter(is_special=True, active=True)[:10]
        return render(request, "product/special_offer_list.html",
                      {"exportal_list": special_exportal, "special_internal": special_internal})


class SpecialOfferListComplete(View):
    def get(self, request):
        special_internal = InternalProduct.objects.filter(is_special=True, active=True)[:10]
        special_exportal = ExportalProduct.objects.filter(is_special=True, active=True)[:10]
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


def MainPictureExportalCreateView(request):
    if request.method == "POST":
        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        print(os.path.join(BASE_DIR, 'ali/file_dir'))
        form = ExportalFileLogoForm(request.POST, request.FILES)
        if form.is_valid():
            file = ExportalFileLogo(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


def MainPictureInternalCreateView(request):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    print(os.path.join(BASE_DIR, 'ali/file_dir'))
    if request.method == "POST":
        form = Y(request.POST, request.FILES)
        if form.is_valid():
            file = FileModel(file=form.cleaned_data["file"])
            file.save()

            return redirect("ali:test1")
    else:
        form = Y()
    return render(request, "test.html", {"form": form})


def MainPictureExportalCreateView(request):
    if request.method == "POST":
        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        print(os.path.join(BASE_DIR, 'ali/file_dir'))
        form = ExportalFileLogoForm(request.POST, request.FILES)
        if form.is_valid():
            file = ExportalFileLogo(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


def PartialPictureInternalCreateView(request):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    print(os.path.join(BASE_DIR, 'ali/file_dir'))
    if request.method == "POST":
        form = ExportalFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = FileModel(file=form.cleaned_data["file"])
            file.save()

            return redirect("ali:test1")
    else:
        form = ExportalFileForm()
    return render(request, "test.html", {"form": form})


def PartialPictureExportalCreateView(request):
    if request.method == "POST":
        form = ExportalFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = ExportalFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


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
            "internal": InternalProduct.objects.all(),
            "exportal": ExportalProduct.objects.all(),
            "lined": LinedProduct.objects.all(),
            "total_count": total_count,
            "total_ton": total_ton
        }
        return render(request, "product/all_product_complete.html", context)


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
        context_data["tonajze"] = InternalProduct.objects.all().aggregate(Sum("approximate_tonnage"))[
            'approximate_tonnage__sum']
        return context_data


def product_detail(request, unique_id):
    context = {"full_path": request.build_absolute_uri() + '?share=1'}
    if request.resolver_match.url_name == 'internal_product_detail':
        context.update({'object': get_object_or_404(InternalProduct, unique_id=unique_id), 'is_internal': 1})
    elif request.resolver_match.url_name == 'exportal_product_detail':
        context.update({'object': get_object_or_404(ExportalProduct, unique_id=unique_id), 'is_exportal': 1})
    elif request.resolver_match.url_name == 'lined_product_detail':
        context.update({'object': get_object_or_404(LinedProduct, unique_id=unique_id), 'is_lined': 1})
    if request.method == 'POST':
        if request.POST.get('submit') == 'hold':
            form = HoldForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Hold()
                obj.user = User.objects.get(id=request.user.id)
                if form.cleaned_data['pin']:
                    obj.pin = form.cleaned_data['pin']
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
        if request.POST.get('submit') == 'visit':
            form = VisitForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Visit()
                obj.user = User.objects.get(id=request.user.id)
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['occupation']:
                    obj.occupation = form.cleaned_data['occupation']
                if form.cleaned_data['company']:
                    obj.company = form.cleaned_data['company']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['address']:
                    obj.address = form.cleaned_data['address']
                if form.cleaned_data['visit_date']:
                    obj.visit_date = form.cleaned_data['visit_date']
                if form.cleaned_data['visit_hour']:
                    obj.visit_hour = form.cleaned_data['visit_hour']
                if form.cleaned_data['visit_minute']:
                    obj.visit_minute = form.cleaned_data['visit_minute']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
        if request.POST.get('submit') == 'sample':
            form = SampleForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Sample()
                obj.user = User.objects.get(id=request.user.id)
                if form.cleaned_data['pin']:
                    obj.pin = form.cleaned_data['pin']
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
    return render(request, "product/product_detail.html", context)


class InternalProductCreateView(View):

    def get(self, request):
        return render(request, "product/add_internal.html")

    def post(self, request):
        internal_resource = Internal_Product_Resource()
        dataset = Dataset()
        new_internal = request.FILES['file']
        imported_data = dataset.load(new_internal.read(), format='xlsx')
        result = internal_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            internal_resource.import_data(dataset, dry_run=False)

        return render(request, "product/add_internal.html")


# class InternalImage(View):
def InternalImage(request):
    if request.method == "POST":
        form = InternalFileLogoForm(request.POST, request.FILES)
        if form.is_valid():
            file = InternalFileLogo(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")
    # def post(self, request):
    #     internal_image_resource = Internal_Product_Image_Resource()
    #     dataset = Dataset()
    #     new_internal_image = request.FILES['file']
    #     imported_data = dataset.load(new_internal_image.read(), format='zip')
    #     for data in imported_data:
    #         print(data[1])
    #         value = Internal_Image(
    #             data[0],
    #             data[1],
    #         )
    #         value.save()
    #     return redirect("config:panel_home")


# Exportal
class ExportalProductPanelList(LoginRequiredMixin, ListView):
    model = ExportalProduct
    template_name = "product/exportal_list_panel.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(ExportalProductPanelList, self).get_context_data(*args, **kwargs)
        context_data["total"] = ExportalProduct.objects.all().count()
        context_data["tonajze"] = ExportalProduct.objects.aggregate(Sum("approximate_tonnage"))[
            'approximate_tonnage__sum']
        return context_data


class ExportalProductListView(LoginRequiredMixin, ListView):
    queryset = ExportalProduct.objects.filter(active=True)[:20]
    template_name = "product/exportal_list.html"


class ExportalProductListCompleteView(LoginRequiredMixin, ListView):
    model = ExportalProduct
    template_name = "product/exportal_list_complete.html"


class ExportalProductCreateView(View):

    def get(self, request):
        return render(request, "product/add_exportal.html")

    def post(self, request):
        internal_resource = Exportal_Product_Resource()
        dataset = Dataset()
        new_exportal = request.FILES['file']
        imported_data = dataset.load(new_exportal.read(), format='xlsx')
        result = internal_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            internal_resource.import_data(dataset, dry_run=False)

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


def PartialPictureInternalCreateView(request):
    if request.method == "POST":
        form = InternalFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = InternalFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


# Lined
class LinedProductList(ListView):
    model = LinedProduct
    template_name = "product/line_list.html"


class LinedProductPanelList(ListView):
    model = LinedProduct
    template_name = "product/line_list.html"


def lined_product_image(request):
    if request.method == "POST":
        form = linedFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = linedFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


class LinedProductCreateView(View):
    def get(self, request):
        return render(request, "product/create_lined.html")

    def post(self, request):
        lined_resource = Lined_Product_Resource()
        dataset = Dataset()
        new_lined = request.FILES['file']
        imported_data = dataset.load(new_lined.read(), format='xlsx')
        result = lined_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            lined_resource.import_data(dataset, dry_run=False)
        return render(request, "product/create_lined.html")


# REJECTED

# class RejectedProductList(ListView):
#     model = Rejected
#     template_name = "product/rejected_list_panel.html"
class RejectedProductList(View):
    def get(self, request):
        queryset = RejectedFilter(request.GET, queryset=Rejected.objects.all())
        return render(request, "product/rejected_list_panel.html", {'filter': queryset})


# Loaded


class LoadedProductList(ListView):
    model = Loaded
    template_name = "product/loaded_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(LoadedProductList, self).get_context_data(*args, **kwargs)
        # context_data["total"]=Loaded.objects.all().count()
        # context_data["tonajze"]=Loaded.objects.aggregate(Sum("weight_of_scales"))
        return context_data


def rejected_update(request):
    return render(request, 'product/rejected_update.html')


def rejected_upload(request):
    if request.method == 'POST':
        rejected_resource = Rejected_Product_Resource()
        dataset = Dataset()
        new_rejected = request.FILES['rejectedData']
        imported_data = dataset.load(new_rejected.read())
        result = rejected_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            rejected_resource.import_data(dataset, dry_run=False)
            for data in imported_data:
                try:
                    if data[7][0] == 'E':
                        obj = ExportalProduct.objects.get(unique_id=data[7][0])
                        obj.active = True
                        obj.rejected = True
                        obj.save()
                    elif data[7][0] == 'D':
                        obj = InternalProduct.objects.get(unique_id=data[7][0])
                        obj.active = True
                        obj.rejected = True
                        obj.save()
                    elif data[7][0] == 'L':
                        obj = LinedProduct.objects.get(unique_id=data[7][0])
                        obj.active = True
                        obj.rejected = True
                        obj.save()
                except:
                    continue
        return redirect("config:panel_home")


def LoadedProductCreateView(request):
    if request.method == 'POST':
        loaded_resource = Loaded_Product_Resource()
        dataset = Dataset()
        new_loaded = request.FILES['loadedData']
        imported_data = dataset.load(new_loaded.read(), format='xlsx')
        result = loaded_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            loaded_resource.import_data(dataset, dry_run=False)  # Actually import now
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


def is_valid_queryparam(param):
    return param != '' and param is not None


def SearchView(request):
    context = {}
    stone_type = request.GET.get('stone_type')
    stone_name = request.GET.get('stone_name')
    mine = request.GET.get('mine')
    color_code = request.GET.get('color_code')

    length_min = request.GET.get('length_min')
    length_max = request.GET.get('length_max')
    height_min = request.GET.get('height_min')
    height_max = request.GET.get('height_max')
    ton = request.GET.get('ton')

    grading_code = request.GET.get('grading_code')
    width_min = request.GET.get("width_min")
    param = False

    queryset = InternalProduct.objects.filter(active=True)
    if is_valid_queryparam(stone_type):
        queryset = queryset.filter(mine__stone_type=stone_type)
        param = True
    if is_valid_queryparam(stone_name):
        queryset = queryset.filter(stone_name=stone_name)
        param = True
    if is_valid_queryparam(mine):
        queryset = queryset.filter(mine__name=mine)
        param = True
    if is_valid_queryparam(grading_code):
        queryset = queryset.filter(grading_code=grading_code)
        param = True
    if is_valid_queryparam(length_max):
        queryset = queryset.filter(length__lte=length_max)
        param = True
    if is_valid_queryparam(length_min):
        queryset = queryset.filter(height__gte=length_min)
        param = True
    if is_valid_queryparam(height_max):
        queryset = queryset.filter(height__lte=height_max)
        param = True
    if is_valid_queryparam(height_min):
        queryset = queryset.filter(height__gte=height_min)
        param = True
    if is_valid_queryparam(width_min):
        queryset = queryset.filter(width__gt=width_min)
        param = True
    if is_valid_queryparam(ton):
        queryset = queryset.filter(approximate_tonnage__gt=ton)
        param = True

    if param:
        internal_product = queryset
    else:
        internal_product = None
    context.update({"internal": internal_product})
    param = False

    queryset = ExportalProduct.objects.filter(active=True)
    if is_valid_queryparam(stone_type):
        queryset = queryset.filter(mine__stone_type=stone_type)
        param = True
    if is_valid_queryparam(stone_name):
        queryset = queryset.filter(stone_name=stone_name)
        param = True
    if is_valid_queryparam(mine):
        queryset = queryset.filter(mine__name=mine)
        param = True
    if is_valid_queryparam(grading_code):
        queryset = queryset.filter(grading_code=grading_code)
        param = True
    if is_valid_queryparam(length_max):
        queryset = queryset.filter(length__lte=length_max)
        param = True
    if is_valid_queryparam(length_min):
        queryset = queryset.filter(height__gte=length_min)
        param = True
    if is_valid_queryparam(height_max):
        queryset = queryset.filter(height__lte=height_max)
        param = True
    if is_valid_queryparam(height_min):
        queryset = queryset.filter(height__gte=height_min)
        param = True
    if is_valid_queryparam(width_min):
        queryset = queryset.filter(width__gt=width_min)
        param = True
    if is_valid_queryparam(ton):
        queryset = queryset.filter(approximate_tonnage__gt=ton)
        param = True
    if is_valid_queryparam(color_code):
        queryset = queryset.filter(color_code=color_code)
        param = True

    if param:
        exportal_product = queryset
    else:
        exportal_product = None
    context.update({"exportal": exportal_product})
    param = False

    queryset = LinedProduct.objects.filter(active=True)
    if is_valid_queryparam(stone_type):
        queryset = queryset.filter(mine__stone_type=stone_type)
        param = True
    if is_valid_queryparam(stone_name):
        queryset = queryset.filter(stone_name=stone_name)
        param = True
    if is_valid_queryparam(mine):
        queryset = queryset.filter(mine__name=mine)
        param = True
    if is_valid_queryparam(grading_code):
        queryset = queryset.filter(grading_code=grading_code)
        param = True
    if is_valid_queryparam(length_max):
        queryset = queryset.filter(length__lte=length_max)
        param = True
    if is_valid_queryparam(length_min):
        queryset = queryset.filter(height__gte=length_min)
        param = True
    if is_valid_queryparam(height_max):
        queryset = queryset.filter(height__lte=height_max)
        param = True
    if is_valid_queryparam(height_min):
        queryset = queryset.filter(height__gte=height_min)
        param = True
    if is_valid_queryparam(width_min):
        queryset = queryset.filter(width__gt=width_min)
        param = True
    if is_valid_queryparam(ton):
        queryset = queryset.filter(approximate_tonnage__gt=ton)
        param = True
    if is_valid_queryparam(color_code):
        queryset = queryset.filter(color_code=color_code)
        param = True

    if param:
        lined_product = queryset
    else:
        lined_product = None
    context.update({"lined": lined_product})

    return render(request, "product/search.html", context)
