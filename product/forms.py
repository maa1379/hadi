from django import forms
from .models import ExportalFile, ExportalFileLogo, InternalFileLogo, linedFile


class ExportalFileForm(forms.ModelForm):
    class Meta:
        model=ExportalFile
        fields="__all__"

class ExportalFileLogoForm(forms.ModelForm):
    class Meta:
        model=ExportalFileLogo
        fields="__all__"

class InternalFileLogoForm(forms.ModelForm):
    class Meta:
        model=InternalFileLogo
        fields="__all__"

class linedFileForm(forms.ModelForm):
    class Meta:
        model=linedFile
        fields="__all__"

        
        
        
