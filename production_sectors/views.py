from django.views.generic import ListView, CreateView
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