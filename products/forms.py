from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['organization', 'subsidiary', 'code', 'name', 'group', 'brand', 'cost_price', 'selling_price', 'unit_measure', 'production_time', 'production_sectors']
        widgets = {
            'organization': forms.Select(attrs={'class': 'form-control', 'default': '1'}),
            'subsidiary': forms.Select(attrs={'class': 'form-control', 'default': '1'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'cost_price': forms.TextInput(attrs={'class': 'form-control'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_measure': forms.Select(attrs={'class': 'form-control'}),
            'production_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'production_sectors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
