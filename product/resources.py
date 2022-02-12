from .models import InternalProduct, ExportalProduct, Internal_Image, Exportal_Image, \
    LinedProduct, Loaded, Rejected

from import_export import resources


class Internal_Product_Resource(resources.ModelResource):
    class Meta:
        model = InternalProduct


class Internal_Product_Image_Resource(resources.ModelResource):
    class Meta:
        model = Internal_Image


class Exportal_Product_Resource(resources.ModelResource):
    class Meta:
        model = ExportalProduct


class Exportal_Product_Image_Resource(resources.ModelResource):
    class Meta:
        model = Exportal_Image


class Lined_Product_Resource(resources.ModelResource):
    class Meta:
        model = LinedProduct


class Loaded_Product_Resource(resources.ModelResource):
    class Meta:
        model = Loaded


class Rejected_Product_Resource(resources.ModelResource):
    class Meta:
        model = Rejected
