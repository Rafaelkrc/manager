from django.views.generic import ListView
from . import models


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
