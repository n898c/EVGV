from django import forms
from django.forms import ModelForm
import calculation
from .models import CarClass

class CarForm(ModelForm):
    class Meta:
        model=CarClass
        fields=['make','carModel','year','make2','carModel2','year2']
        


