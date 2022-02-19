from .models import *

from import_export import resources


class Internal_Product_Resource(resources.ModelResource):
    class Meta:
        model = InternalProduct


class Exportal_Product_Resource(resources.ModelResource):
    class Meta:
        model = ExportalProduct


class Exportal_Product_Image_Resource(resources.ModelResource):
    class Meta:
        model = Exportal_Image


class LinedProductMemberResource(resources.ModelResource):
    class Meta:
        model = LinedProductMember


class Loaded_Product_Resource(resources.ModelResource):
    class Meta:
        model = Loaded


class Rejected_Product_Resource(resources.ModelResource):
    class Meta:
        model = Rejected
