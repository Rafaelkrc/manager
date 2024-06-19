from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models, forms


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


class DispatchProductionCreateView(CreateView):
    model = models.DispatchProduction
    form_class = forms.DispatchProductionForm
    template_name = 'dispatch_production_create.html'
    success_url = reverse_lazy('dispatch_production_list')
