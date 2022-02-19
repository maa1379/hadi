from django.contrib import admin
from .models import ExportalProduct, InternalProduct, ProductBase, Exportal_Image, Loaded, \
    LinedProducts, Rejected, InternalMainPic, ExportalMainPic, ExportalGalleries, InternalGalleries, \
    InternalMainPicFile

from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Rejected)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Loaded)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(ExportalProduct)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(InternalProduct)
class PersonAdmin(ImportExportModelAdmin):
    pass


admin.site.register(LinedProducts),
admin.site.register(InternalMainPic),
admin.site.register(ExportalMainPic),
admin.site.register(InternalMainPicFile),
admin.site.register(ProductBase),
admin.site.register(Exportal_Image),
# admin.site.register(Loaded),

admin.site.register(ExportalGalleries),
admin.site.register(InternalGalleries)
# admin.site.register(Rejected),
