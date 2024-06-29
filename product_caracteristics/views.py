from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


class GroupUpdateView(UpdateView):
    model = models.Group
    form_class = forms.GroupForm
    template_name = 'group_update.html'
    success_url = reverse_lazy('group_list')


class GroupDeleteView(DeleteView):
    model = models.Group
    template_name = 'group_delete.html'
    success_url = reverse_lazy('group_list')


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


class BrandUpdateView(UpdateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'brand_update.html'
    success_url = reverse_lazy('brand_list')


class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context['name'] = brand.name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Brand is already related, cannot be deleted!")
            return render(request, 'brand_undelete.html', context)


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


class UnitMeasureUpdateView(UpdateView):
    model = models.UnitMeasure
    form_class = forms.UnitMeasureForm
    template_name = 'unitmeasure_update.html'
    success_url = reverse_lazy('unitmeasure_list')


class UnitMeasureDeleteView(DeleteView):
    model = models.UnitMeasure
    template_name = 'unitmeasure_delete.html'
    success_url = reverse_lazy('unitmeasure_list')
