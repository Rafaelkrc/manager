from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


class DispatchProductionDetailView(DetailView):
    model = models.DispatchProduction
    template_name = 'dispatch_production_detail.html'


class DispatchProductionUpdateView(UpdateView):
    model = models.DispatchProduction
    form_class = forms.DispatchProductionForm
    template_name = 'dispatch_production_update.html'
    success_url = reverse_lazy('dispatch_production_list')


class DispatchProductionDeleteView(DeleteView):
    model = models.DispatchProduction
    template_name = 'dispatch_production_delete.html'
    success_url = reverse_lazy('dispatch_production_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dispatch_production = self.get_object()
        context['po'] = dispatch_production.po
        context['product'] = dispatch_production.product
        context['quantity'] = dispatch_production.quantity
        context['created_at'] = dispatch_production.created_at
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Product linked to a production movement, cannot be deleted!")
            return render(request, 'product_undelete.html', context)
