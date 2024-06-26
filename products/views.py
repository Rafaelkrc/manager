from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        code = self.request.GET.get('code')
        group = self.request.GET.get('group')
        brand = self.request.GET.get('brand')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if code:
            queryset = queryset.filter(code__icontains=code)
        if group:
            queryset = queryset.filter(group__icontains=group)
        if brand:
            queryset = queryset.filter(brand__icontains=brand)
        return queryset


class ProductCreateView(CreateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    context_object_name = 'product_details'


class ProductUpdateView(UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['code'] = product.code
        context['name'] = product.name
        context['group'] = product.group
        context['brand'] = product.brand
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Product linked to a movement, cannot be deleted!")
            return render(request, 'product_undelete.html', context)
