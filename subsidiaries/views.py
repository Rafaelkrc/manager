from django.views.generic import ListView
from . import models


class SubsidiaryListView(ListView):
    model = models.Subsidiary
    template_name = 'subsidiary_list.html'
    context_object_name = 'subsidiaries'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id', 'name')
        name = self.request.GET.get('name')
        register = self.request.GET.get('register')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if register:
            queryset = queryset.filter(register__icontains=register)
        return queryset
