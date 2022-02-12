from django.contrib import admin
from .models import ExportalProduct, InternalProduct, ProductBase, Internal_Image, Exportal_Image ,Loaded,LinedProduct,LinedProduct,Rejected

# Register your models here.

admin.site.register(ExportalProduct,BookAdmin),
admin.site.register(InternalProduct),
admin.site.register(ProductBase),
admin.site.register(Internal_Image),
admin.site.register(Exportal_Image),
admin.site.register(Loaded),
admin.site.register(LinedProduct),
admin.site.register(Rejected),
