from django.views.generic import ListView
from . import models


class DispatchProductionListView(ListView):
    model = models.DispatchProduction
    template_name = 'dispatch_production_list.html'
    context_object_name = 'dispatch_productions'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('po')
        po = self.request.GET.get('po')
        product = self.request.GET.get('product')
        if po:
            queryset = queryset.filter(po__icontains=po)
        if product:
            queryset = queryset.filter(product__name__icontains=product)
        return queryset
