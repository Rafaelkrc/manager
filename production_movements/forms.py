from django import forms
from . import models


class ProductionMovementForm(forms.ModelForm):

    class Meta:
        model = models.ProductionMovement
        fields = ['po', 'quantity', 'description', 'employee', 'origin_sector', 'priority', 'destynation_sector', 'destynation_employee']
        widgets = {
            'po': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'origin_sector': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'destynation_sector': forms.Select(attrs={'class': 'form-control'}),
            'destynation_employee': forms.Select(attrs={'class': 'form-control'})
        }
