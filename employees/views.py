from django.views.generic import ListView
from . import models


class EmployeeListView(ListView):
    model = models.Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('nome')
        register = self.request.GET.get('register')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if register:
            queryset = queryset.filter(regiter__incontains=name)
        return queryset
