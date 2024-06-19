from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from . import models, forms


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


class GroupCreateView(CreateView):
    model = models.Group
    form_class = forms.GroupForm
    template_name = 'group_create.html'
    success_url = reverse_lazy('group_list')


class GroupDetailView(DetailView):
    model = models.Group
    template_name = 'group_detail.html'


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands_list'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(CreateView):
    models = models.Brand
    form_class = forms.BrandForm
    template_name = 'brand_create.html'
    success_url = reverse_lazy('brand_list')


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'


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


class UnitMeasureCreateView(CreateView):
    model = models.UnitMeasure
    form_class = forms.UnitMeasureForm
    template_name = 'unitmeasure_create.html'
    success_url = reverse_lazy('unitmeasure_list')


class UnitMeasureDetailView(DetailView):
    model = models.UnitMeasure
    template_name = 'unitmeasure_detail.html'
