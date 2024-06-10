from django.views.generic import ListView
from . import models


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
