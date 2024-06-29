from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class ProductionSectorListView(ListView):
    model = models.ProductionSector
    template_name = 'production_sector_list.html'
    context_object_name = 'production_sectors'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('ordering')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ProductionSectorCreateView(CreateView):
    model = models.ProductionSector
    form_class = forms.ProductionSectorForm
    template_name = 'production_sector_create.html'
    success_url = reverse_lazy('production_sector_list')


class ProductionSectorDetailView(DetailView):
    model = models.ProductionSector
    template_name = 'production_sector_detail.html'


class ProductionSectorUpdateView(UpdateView):
    model = models.ProductionSector
    form_class = forms.ProductionSectorForm
    template_name = 'production_sector_update.html'
    success_url = reverse_lazy('production_sector_list')


class ProductionSectorDeleteView(DeleteView):
    model = models.ProductionSector
    template_name = 'production_sector_delete.html'
    success_url = reverse_lazy('production_sector_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        production_sector = self.get_object()
        context['name'] = production_sector.name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Production Sector is already related to flows, cannot be deleted!")
            return render(request, 'production_sector_undelete.html', context)
