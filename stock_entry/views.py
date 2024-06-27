from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class StockEntryListView(ListView):
    model = models.StockEntry
    template_name = 'stock_entry_list.html'
    context_object_name = 'stock_entries'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        po = self.request.GET.get('productionmovement')
        name = self.request.GET.get('name')
        if po:
            queryset = queryset.filter(productionmovement__po=po)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class StockEntryCreateView(CreateView):
    model = models.StockEntry
    template_name = 'stock_entry_create.html'
    form_class = forms.StockEntryForm
    success_url = reverse_lazy('stock_entry_list')


class StockEntryDetailView(DetailView):
    model = models.StockEntry
    template_name = 'stock_entry_detail.html'


class StockEntryUpdateView(UpdateView):
    model = models.StockEntry
    form_class = forms.StockEntryForm
    template_name = 'stock_entry_update.html'
    success_url = reverse_lazy('stock_entry_list')


class StockEntryDeleteView(DeleteView):
    model = models.StockEntry
    template_name = 'stock_entry_delete.html'
    success_url = reverse_lazy('stock_entry_list')
