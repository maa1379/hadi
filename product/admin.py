from django.contrib import admin
from .models import ExportalProduct, InternalProduct, ProductBase, Internal_Image, Exportal_Image, Loaded, LinedProduct, \
    LinedProduct, Rejected, InternalLogo, ExportalLogo, ImageExportalModel, ImageInternalModel, ImageLinedModel, \
    linedFile, InternalFileLogo

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


admin.site.register(LinedProduct),
admin.site.register(InternalLogo),
admin.site.register(ExportalLogo),
admin.site.register(InternalFileLogo),
admin.site.register(ProductBase),
admin.site.register(Internal_Image),
admin.site.register(Exportal_Image),
# admin.site.register(Loaded),

admin.site.register(ImageExportalModel),
admin.site.register(ImageLinedModel),
admin.site.register(linedFile),
admin.site.register(ImageInternalModel)
# admin.site.register(Rejected),
