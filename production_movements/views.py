from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class ProductionMovementListView(ListView):
    model = models.ProductionMovement
    template_name = 'production_movements_list.html'
    context_object_name = 'production_movements'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('po')
        po = self.request.GET.get('po')
        employee = self.request.GET.get('employee')
        origin_sector = self.request.GET.get('origin_sector')
        if po:
            queryset = queryset.filter(po=po)
        if employee:
            queryset = queryset.filter(employee__name__icontains=employee)
        if origin_sector:
            queryset = queryset.filter(origin_sector__name__icontains=origin_sector)
        return queryset


class ProductionMovementCreateView(CreateView):
    model = models.ProductionMovement
    form_class = forms.ProductionMovementForm
    template_name = 'production_movements_create.html'
    success_url = reverse_lazy('production_movement_list')


class ProductionMovementDetailView(DetailView):
    model = models.ProductionMovement
    template_name = 'production_movements_detail.html'


class ProductionMovementUpdateView(UpdateView):
    model = models.ProductionMovement
    form_class = forms.ProductionMovementForm
    template_name = 'production_movements_update.html'
    success_url = reverse_lazy('production_movement_list')


class ProductionMovementDeleteView(DeleteView):
    model = models.ProductionMovement
    template_name = 'production_movements_delete.html'
    success_url = reverse_lazy('production_movement_list')
