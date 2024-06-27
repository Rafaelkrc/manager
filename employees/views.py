from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


class EmployeeUpdateView(UpdateView):
    model = models.Employee
    form_class = forms.EmployeeForm
    template_name = 'employee_update.html'
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(DeleteView):
    model = models.Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_object()
        context['name'] = employee.name
        context['register'] = employee.register
        context['email'] = employee.email
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Cannot delete this employee because it has protected dependencies.")
            return render(request, 'employee_undelete.html', context)
