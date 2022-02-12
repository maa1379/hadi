from django.db import models
from mine.models import Mine
from django.db.models import Sum
from django.db.models.signals import post_save
import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from PIL import Image
from django.conf import settings
from zipfile import ZipFile
from chardet import detect as charsetdetect
from wheel.util import native

GALLERIES_UPLOAD_DIR = "galleries"



class ImageLinedModel(models.Model):
    photo = models.ImageField(upload_to="images")
    name=models.CharField(max_length=100,blank=True,null=True)
    product=models.ForeignKey('LinedProduct', on_delete=models.CASCADE,related_name="image_lined")
    
    def save(self, *args, **kwargs):
        p=LinedProduct.objects.get(id=name)
        self.product=p
        super(ImageInternalModel, self).save(*args, **kwargs)


class linedFile(models.Model):
    file = models.FileField(upload_to="file/")

    def save(self, delete_zip_import=True, *args, **kwargs):
        """
        If a zip file is uploaded, extract any images from it and add
        them to the gallery, before removing the zip file.
        """
        super().save(*args, **kwargs)
        if self.file:
            zip_file = ZipFile(self.file)
            for name in zip_file.namelist():
                data = zip_file.read(name)
                try:
                    from PIL import Image
                    image = Image.open(BytesIO(data))
                    image.load()
                    image = Image.open(BytesIO(data))
                    image.verify()
                except ImportError:
                    pass
                except:  # noqa
                    continue
                name = os.path.split(name)[1]

                # In python3, name is a string. Convert it to bytes.
                if not isinstance(name, bytes):
                    try:
                        name = name.encode("cp437")
                    except UnicodeEncodeError:
                        # File name includes characters that aren't in cp437,
                        # which isn't supported by most zip tooling. They will
                        # not appear correctly.
                        tempname = name

                # Decode byte-name.
                if isinstance(name, bytes):
                    encoding = charsetdetect(name)["encoding"]
                    tempname = name.decode(encoding)

                # to / on disk; see os.path.join docs.
                path = os.path.join(GALLERIES_UPLOAD_DIR, tempname)
                try:
                    saved_path = default_storage.save(path, ContentFile(data))
                except UnicodeEncodeError:
                    from warnings import warn

                    warn(
                        "A file was saved that contains unicode "
                        "characters in its path, but somehow the current "
                        "locale does not support utf-8. You may need to set "
                        "'LC_ALL' to a correct value, eg: 'en_US.UTF-8'."
                    )
                    # The native() call is needed here around str because
                    # os.path.join() in Python 2.x (in posixpath.py)
                    # mixes byte-strings with unicode strings without
                    # explicit conversion, which raises a TypeError as it
                    # would on Python 3.
                    path = os.path.join(
                        GALLERIES_UPLOAD_DIR, slug, str(name, errors="ignore")
                    )
                    saved_path = default_storage.save(path, ContentFile(data))
                images = ImageLinedModel(photo=saved_path)
                pic_name = str(self.images)
                ali = pic_name.split('/')[1]
                images.name=ali[:4]
                images.save()
            if delete_zip_import:
                zip_file.close()
                self.file.delete(save=True)









class InternalLogo(models.Model):
    photo = models.ImageField(upload_to="images")
    product=models.ForeignKey('InternalProduct', on_delete=models.CASCADE,related_name="image_internal_logo")

class ExportalLogo(models.Model):
    photo = models.ImageField(upload_to="images")
    product=models.ForeignKey('ExportalProduct', on_delete=models.CASCADE,related_name="image_exportal_logo")

    
class ImageInternalModel(models.Model):
    photo = models.ImageField(upload_to="images")
    name=models.CharField(max_length=100,blank=True,null=True)
    product=models.ForeignKey('InternalProduct', on_delete=models.CASCADE,related_name="image_internal")
    
    def save(self, *args, **kwargs):
        p=InternalProduct.objects.get(serial_number_of_the_peak_in_the_mine=name)
        self.product=p
        super(ImageInternalModel, self).save(*args, **kwargs)
    
    
    
class InternalFile(models.Model):
    file = models.FileField(upload_to="file/")

    def save(self, delete_zip_import=True, *args, **kwargs):
        """
        If a zip file is uploaded, extract any images from it and add
        them to the gallery, before removing the zip file.
        """
        super().save(*args, **kwargs)
        if self.file:
            zip_file = ZipFile(self.file)
            for name in zip_file.namelist():
                data = zip_file.read(name)
                try:
                    from PIL import Image
                    image = Image.open(BytesIO(data))
                    image.load()
                    image = Image.open(BytesIO(data))
                    image.verify()
                except ImportError:
                    pass
                except:  # noqa
                    continue
                name = os.path.split(name)[1]

                # In python3, name is a string. Convert it to bytes.
                if not isinstance(name, bytes):
                    try:
                        name = name.encode("cp437")
                    except UnicodeEncodeError:
                        # File name includes characters that aren't in cp437,
                        # which isn't supported by most zip tooling. They will
                        # not appear correctly.
                        tempname = name

                # Decode byte-name.
                if isinstance(name, bytes):
                    encoding = charsetdetect(name)["encoding"]
                    tempname = name.decode(encoding)

                # to / on disk; see os.path.join docs.
                path = os.path.join(GALLERIES_UPLOAD_DIR, tempname)
                try:
                    saved_path = default_storage.save(path, ContentFile(data))
                except UnicodeEncodeError:
                    from warnings import warn

                    warn(
                        "A file was saved that contains unicode "
                        "characters in its path, but somehow the current "
                        "locale does not support utf-8. You may need to set "
                        "'LC_ALL' to a correct value, eg: 'en_US.UTF-8'."
                    )
                    # The native() call is needed here around str because
                    # os.path.join() in Python 2.x (in posixpath.py)
                    # mixes byte-strings with unicode strings without
                    # explicit conversion, which raises a TypeError as it
                    # would on Python 3.
                    path = os.path.join(
                        GALLERIES_UPLOAD_DIR, slug, str(name, errors="ignore")
                    )
                    saved_path = default_storage.save(path, ContentFile(data))
                images = ImageInternalModel(photo=saved_path)
                pic_name = str(self.images)
                ali = pic_name.split('/')[1]
                images.name=ali[:4]
                images.save()
            if delete_zip_import:
                zip_file.close()
                self.file.delete(save=True)


class ImageExportalModel(models.Model):
    photo = models.ImageField(upload_to="images")
    name=models.CharField(max_length=100,blank=True,null=True)
    product=models.ForeignKey('ExportalProduct', on_delete=models.CASCADE,related_name="image_exportal")
    
    def save(self, *args, **kwargs):
        p=ExportalProduct.objects.get(serial_number_of_the_peak_in_the_mine=name)
        self.product=p
        super(ImageExportalModel, self).save(*args, **kwargs)
    
    
    
    



class ExportalFile(models.Model):
    file = models.FileField(upload_to="file/")

    def save(self, delete_zip_import=True, *args, **kwargs):
        """
        If a zip file is uploaded, extract any images from it and add
        them to the gallery, before removing the zip file.
        """
        super().save(*args, **kwargs)
        if self.file:
            zip_file = ZipFile(self.file)
            for name in zip_file.namelist():
                data = zip_file.read(name)
                try:
                    from PIL import Image

                    image = Image.open(BytesIO(data))
                    image.load()
                    image = Image.open(BytesIO(data))
                    image.verify()
                except ImportError:
                    pass
                except:  # noqa
                    continue
                name = os.path.split(name)[1]

                # In python3, name is a string. Convert it to bytes.
                if not isinstance(name, bytes):
                    try:
                        name = name.encode("cp437")
                    except UnicodeEncodeError:
                        # File name includes characters that aren't in cp437,
                        # which isn't supported by most zip tooling. They will
                        # not appear correctly.
                        tempname = name

                # Decode byte-name.
                if isinstance(name, bytes):
                    encoding = charsetdetect(name)["encoding"]
                    tempname = name.decode(encoding)

                # to / on disk; see os.path.join docs.
                path = os.path.join(GALLERIES_UPLOAD_DIR, tempname)
                try:
                    saved_path = default_storage.save(path, ContentFile(data))
                except UnicodeEncodeError:
                    from warnings import warn

                    warn(
                        "A file was saved that contains unicode "
                        "characters in its path, but somehow the current "
                        "locale does not support utf-8. You may need to set "
                        "'LC_ALL' to a correct value, eg: 'en_US.UTF-8'."
                    )
                    # The native() call is needed here around str because
                    # os.path.join() in Python 2.x (in posixpath.py)
                    # mixes byte-strings with unicode strings without
                    # explicit conversion, which raises a TypeError as it
                    # would on Python 3.
                    path = os.path.join(
                        GALLERIES_UPLOAD_DIR, slug, str(name, errors="ignore")
                    )
                    saved_path = default_storage.save(path, ContentFile(data))
                images = ImageExportalModel(photo=saved_path)
                name = str(self.images)
                ali = name.split('/')[1]
                images.name=ali[:4]
                images.save()
            if delete_zip_import:
                zip_file.close()
                self.file.delete(save=True)





# Create your models here.
class ProductBase(models.Model):
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    stone_name = models.CharField(max_length=125)
    created = models.DateField()
    working_breast_code = models.CharField(max_length=125)
    serial_number_of_the_peak_in_the_mine = models.CharField(max_length=125)
    add = models.DateField(auto_now_add=True)
    approximate_tonnage = models.PositiveIntegerField()
    unique_id = models.CharField(max_length=255)
    is_special = models.BooleanField(default=False)
    length = models.PositiveIntegerField(null=True,blank=True)
    width = models.PositiveIntegerField(null=True,blank=True)
    height = models.PositiveIntegerField(null=True,blank=True)
    stair_code = models.CharField(max_length=10)
    buyer = models.CharField(max_length=255, null=True, blank=True)
    grading_code = models.CharField(max_length=10)


class InternalProduct(ProductBase):
#     lined = models.BooleanField(default=False)
    product_name=models.CharField(max_length=25,null=True,blank=True)

    def get_first_image(self):
        return self.image.first()

    def __str__(self):
        return self.stone_name


class Internal_Image(models.Model):
    photo = models.ImageField(upload_to="image/product/")
    product_name = models.ForeignKey(InternalProduct, on_delete=models.CASCADE, related_name="image",null=True,blank=True)


class ExportalProduct(ProductBase):
    color_code = models.CharField(max_length=10)
    code_Slate = models.CharField(max_length=10)

    def related_count(self):
        exportal = ExportalProduct.objects.filter(grading_code=self.grading_code, color_code=self.color_code,
                                                  code_Slate=self.code_Slate).count()
        return exportal

    # Weight_of_scales = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.stone_name


class Exportal_Image(models.Model):
    photo = models.ImageField(upload_to="image/product/")
    product_name = models.ForeignKey(ExportalProduct, on_delete=models.CASCADE, related_name="image")


class Loaded(models.Model):
    transport_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    freight_number = models.CharField(max_length=125)
    weight_of_scales = models.PositiveIntegerField()
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    buyer = models.CharField(max_length=255)
    serial_number_of_the_peak_in_the_mine = models.CharField(max_length=125)


class LinedProduct(models.Model):
    line_number = models.CharField(max_length=125)

    def get_line_total(self):
        return InternalProduct.objects.filter(line_number=self.line_number).aggregate(Sum("approximate_tonnage"))


class Rejected(models.Model):
    transport_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    freight_number = models.CharField(max_length=125)
    weight_of_scales = models.PositiveIntegerField()
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
    buyer = models.CharField(max_length=255)
    serial_number_of_the_peak_in_the_mine = models.CharField(max_length=125)

    
    
    
