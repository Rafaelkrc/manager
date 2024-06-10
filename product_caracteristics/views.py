from django.views.generic import ListView
from . import models


class GroupListView(ListView):
    model = models.Group
    template_name = 'group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class UnitMeasureListView(ListView):
    model = models.UnitMeasure
    template_name = 'unitmeasure_list.html'
    context_object_name = 'untimeasures'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
