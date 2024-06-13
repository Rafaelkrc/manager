from django import forms
from . import models


class ProductionSectorForm(forms.ModelForm):

    class Meta:
        model = models.ProductionSector
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'ordering': forms.TextInput(attrs={'class': 'form-control'}),
        }
