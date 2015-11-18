from django import forms
from django.forms import ModelForm
from aplic.models import *

class ParametroForm(forms.Form):
    pass

class ClienteForm(ModelForm): 
   class Meta:
        model=Cliente
        exclude=["eliminado"]

