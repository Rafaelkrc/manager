from django import forms
from . import models


class GroupForm(forms.ModelForm):

    class Meta:
        model = models.Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UnitMeasureForm(forms.ModelForm):

    class Meta:
        model = models.UnitMeasure
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abbreviation': forms.TextInput(attrs={'class': 'form-control'}),
        }
