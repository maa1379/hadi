from django import forms
from .models import  ExportalFile,ExportalFileLogo

class ExportalFileForm(forms.ModelForm):
    class Meta:
        model=ExportalFile
        fields="__all__"

class ExportalFileLogoForm(forms.ModelForm):
    class Meta:
        model=ExportalFileLogo
        fields="__all__"

        
        
        
