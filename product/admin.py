from django.contrib import admin
from .models import ExportalProduct, InternalProduct, ProductBase, Internal_Image, Exportal_Image ,Loaded,LinedProduct,LinedProduct,Rejected
from import_export.admin import ExportActionMixin
# Register your models here.
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('slate_code',)
admin.site.register(BookAdmin,ExportalProduct),
admin.site.register(InternalProduct),
admin.site.register(ProductBase),
admin.site.register(Internal_Image),
admin.site.register(Exportal_Image),
admin.site.register(Loaded),
admin.site.register(LinedProduct),
admin.site.register(Rejected),
