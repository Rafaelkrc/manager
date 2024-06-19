from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from . import models, forms


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


class EmployeeCreateView(CreateView):
    model = models.Employee
    form_class = forms.EmployeeForm
    template_name = 'employee_create.html'
    success_url = reverse_lazy('employee_list')


class EmployeeDetailView(DetailView):
    model = models.Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee_details'
